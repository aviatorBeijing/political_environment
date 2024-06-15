from cmath import rect
import os, click,datetime,json,enum
from tabulate import tabulate
import numpy as np
import pandas as pd

from sqlalchemy import create_engine, text
import pandas as pd
from decimal import Decimal

uname = os.getenv('PG_USERNAME', '')
psw = os.getenv('PG_PASSWORD', '')

eng = create_engine( f"postgresql://{uname}:{psw}@localhost:5432/china_politics")
tbname = 'unnatural_death'
cols = 'name,occupation,nationality,death_date,reason,source_info'

def table_exists(  ):
    _engine = eng
    assert _engine, "error"
    stmt = f'''
SELECT EXISTS 
(               
        SELECT 1                       
        FROM information_schema.tables 
        WHERE table_name = '{tbname}'      
);
    '''                                        
    df = pd.read_sql(stmt, _engine)
    tbname_exists = df.iloc[0].exists
                                                              
    if tbname_exists: # Not only table exists, but also not empty
        stmt = f'SELECT FROM "{tbname}"'                                                                                
        with _engine.connect() as conn:                             
            rst = conn.execute( text(stmt ) )
            rows = rst.fetchall()  
            if len(rows)>0:                                 
                return True                                             
    return False               

def _exec(stmt):
    with eng.connect() as conn:
        rst = conn.execute( text(stmt) )
        conn.commit()
        rows = []
        if stmt.upper().startswith('SELECT'):
            if rst:
                for row in rst.fetchall():
                    rows += [ row ]
    return rows 

class DeathReason(enum.Enum):
    SUICIDE = 'suicide'
    SENTENCED = 'sentenced'
    KILLED_BY_RIVAL = 'killed_by_rival'
    KILLED_BY_LEADER = 'killed_by_leader'

def add_one( name,occupation,nationality:str,death_date,reason:DeathReason, source_info:str):
    df = pd.DataFrame.from_records([[ name,occupation,nationality,death_date,reason.value,source_info]])
    df.columns = 'name,occupation,nationality,death_date,reason,source_info'.split(',')
    
    with eng.connect()  as conn:
        if not table_exists():
            df.to_sql(tbname,conn,index=0)
            _exec(f'ALTER TABLE {tbname} ADD PRIMARY KEY (name,death_date);')
        else:
            _exec(f"""
INSERT INTO {tbname} ({cols})
VALUES ('{name}','{occupation}','{nationality}',{death_date},'{reason.value}','{source_info}' )
ON CONFLICT (name,death_date) 
DO UPDATE SET occupation='{occupation}',nationality='{nationality}',reason='{reason.value}',source_info='{source_info}'""")
        
        recs = _exec(f'SELECT * FROM {tbname}')
        df = pd.DataFrame.from_records(recs,columns=cols.split(','))
        print( tabulate(df, headers='keys') )

    
@click.command()
@click.option('--show',is_flag=True, default=False)
@click.option('--name')
@click.option('--occupation')
@click.option('--nation')
@click.option('--death_date')
@click.option('--reason')
@click.option('--source')
def main(show,name,occupation,nation,death_date,reason,source):
    if show:
        recs = _exec(f'SELECT * FROM {tbname}')
        df = pd.DataFrame.from_records(recs,columns=cols.split(','))
        df.death_date = df.death_date.apply(int)
        df = df.sort_values('death_date', ascending=False)
        print( tabulate(df, headers='keys') )

        recs = _exec(f'SELECT nationality,COUNT(nationality) FROM {tbname} GROUP BY nationality;')
        print( tabulate( pd.DataFrame.from_records(recs,columns=['nationality', '#'] ).sort_values('#').reset_index(drop=True), headers='keys' ) )
    else:
        reason = DeathReason(reason)
        add_one( name,occupation,nation,death_date,reason,source )

if __name__ == '__main__':
    main()
