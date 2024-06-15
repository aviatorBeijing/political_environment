## The Most Famous Deaths Throughout Chinese History
### Addition:
```
python src/unnatural_death/historical.py --name <name> --occupation "<personal/occupation/when/desceased>" --nation <gov. when death sentence was initiated.> --death_date=<year of death> --reason <enum> --source <source of the information>
```
### Reason (enum)
```
class DeathReason(enum.Enum):
    SUICIDE = 'suicide'
    SENTENCED = 'sentenced'
    KILLED_BY_RIVAL = 'killed_by_rival'
    KILLED_BY_LEADER = 'killed_by_leader'
```

### List
```
python src/unnatural_death/historical.py --show
```
