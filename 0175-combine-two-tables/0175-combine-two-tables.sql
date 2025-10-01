# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state
from address a right join person p
on p.personId=a.personId;
