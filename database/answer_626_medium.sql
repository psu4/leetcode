SELECT 
y.preid as id, 
y.student
FROM (
SELECT 
id,
case when (id % 2=0) then @preid:=id-1
     else @preid:=if(id<>(select max(id) from seat),id+1,id)
     end preid, 
student
FROM
seat,
    (select @preid:=1) x 
) y order by y.preid ASC;

## my answer avoids <> 1 negative search, which improves the performance and beats 92% of the submmited answers
