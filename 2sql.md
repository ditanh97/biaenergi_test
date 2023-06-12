# 2. SQL
Answer:

```
Select USA.NAME, EU.NAME From USA, EU Where USA.ID = EU.ID
```

| USA.NAME         | EU.NAME          | 
| ---------------- | ---------------- | 
| Thomas           | Thomas           | 

```
Select USA.NAME, EU.NAME From USA left join EU Where USA.ID = EU.ID
```


| USA.NAME         | EU.NAME          | 
| ---------------- | ---------------- | 
| Thomas           | Thomas           | 
| Cindy            | Null             | 


```
Select USA.NAME, EU.NAME From USA,  EU
```


| USA.NAME         | EU.NAME          | 
| ---------------- | ---------------- | 
| Thomas           | Francois         | 
| Thomas           | Thomas           | 
| Cindy            | Francois         | 
| Cindy            | Thomas           | 





- The concern with this design if it required to not only store customer data in usa or eu, but need the data in different region or country. So it is not optimized to add new table just to store the same data (which is basically they store same data. e.i id and name) 
- It can be optimized by using one table for persisting customer data i.e TT_CUSTOMER (consist of `id`, `name`,`country_id`) and one table for storing region or country data i.e M_REGION (`id`, `name`) where `country_id` in TT_CUSTOMER is indicating `id` in M_REGION 
