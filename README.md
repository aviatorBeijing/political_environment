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
### Examples
```
 8  李大钊        教授                    北洋政府               1927  killed_by_leader  百度词条
 7  刘和珍        大学生                  北洋政府               1926  killed_by_leader  百度词条
 6  岳云          将领                    赵宋                   1142  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg247
 5  张宪          将领                    赵宋                   1142  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg247
 4  岳飞          统帅                    赵宋                   1142  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg248
 3  刘允升        进士                    赵宋                   1142  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg248
 1  陈东(少阳)    文人太学生              赵宋                   1127  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg32
 2  欧阳澈(德明)  文人                    赵宋                   1127  killed_by_leader  荒淫无道宋高宗(王曾瑜)pg32
 0  武元衡        宰相                    李唐                    815  killed_by_rival   旧唐书卷108

```
