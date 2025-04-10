# Write your MySQL query statement below
Select P.lastName, P.firstName, A.city, A.state from Person P
left Join Address A On P.personId = A.personId