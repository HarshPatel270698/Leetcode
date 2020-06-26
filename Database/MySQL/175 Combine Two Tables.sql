/*
175. Combine Two Tables
**********
Problem Link : https://leetcode.com/problems/combine-two-tables/
Solution Link : https://leetcode.com/submissions/detail/295461353/
Runtime: 501 ms
Memory Usage: 0B
**********
*/
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;
