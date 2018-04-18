select a.FirstName, a.LastName, b.City, b.State

FROM Person a

LEFT JOIN Address b 
on a.PersonId = b.PersonId;
