use sakila;

#1a. Display the first and last names of all actors from the table actor.
select first_name,last_name from actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select concat(first_name,' ',last_name) as Actor_Name from actor;

#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
#What is one query would you use to obtain this information?
select actor_id,first_name,last_name from actor where first_name = 'Joe';

#2b. Find all actors whose last name contain the letters GEN:
select * from actor where last_name like '%GEN%';

#2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select last_name,first_name from actor where last_name like '%LI%';

#2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id,country from country where country_id and country in ('Afghanistan','Bangladesh','China');

#3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
alter table actor add column middle_name varchar(255) after first_name;

#3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
alter table actor modify column middle_name blob;

#3c. Now delete the middle_name column.
alter table actor drop column middle_name;

#4a. List the last names of actors, as well as how many actors have that last name.
select last_name,count(last_name) from actor group by last_name;

#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name,count(last_name) from actor group by last_name having count(last_name)>2;

#4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, 
#the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
update actor set first_name = 'HARPO'
where actor_id = 172;

#4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
#In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. 
#Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
#BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
update actor set first_name = 'GROUCHO'
where first_name = 'HARPO' and last_name = 'WILLIAMS';

#5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
show create table address;

#6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select staff.first_name,staff.last_name,address.address from staff left join address on staff.address_id = address.address_id;

#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select staff.first_name, staff.last_name, sum(payment.amount)
from staff
left join payment on staff.staff_id = payment.staff_id
where payment_date like '%2005-08%'
GROUP BY staff.first_name, staff.last_name;

#6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select film.title, count(film_actor.actor_id)
from film 
inner join film_actor on film.film_id = film_actor.film_id
group by film.title;

#6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select total from (select film.title, count(film_actor.actor_id) as total
from film 
inner join film_actor on film.film_id = film_actor.film_id
group by film.title) as f
where title = 'Hunchback Impossible';

#6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select c.last_name,c.first_name, sum(p.amount) as amount_payed
from customer as c
left join payment as p on c.customer_id = p.customer_id
group by c.last_name,c.first_name
order by c.last_name;

#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
#As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
#Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select title
from film
where (title like 'K%' or 'Q%') 
and language_id = 
(
select language_id 
from language
where name =  'English'
);

# 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name
FROM actor
WHERE actor_id
IN (SELECT actor_id FROM film_actor WHERE film_id 
IN (SELECT film_id from film where title='ALONE TRIP'));

#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. 
#Use joins to retrieve this information.
SELECT first_name, last_name, email 
FROM customer cu
JOIN address a ON (cu.address_id = a.address_id)
JOIN city cit ON (a.city_id=cit.city_id)
JOIN country cntry ON (cit.country_id=cntry.country_id);

#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
#Identify all movies categorized as famiy films.
SELECT title from film f
JOIN film_category fcat on (f.film_id=fcat.film_id)
JOIN category c on (fcat.category_id=c.category_id);

#7e. Display the most frequently rented movies in descending order.
SELECT title, COUNT(f.film_id) AS 'Count_of_Rented_Movies'
FROM  film f
JOIN inventory i ON (f.film_id= i.film_id)
JOIN rental r ON (i.inventory_id=r.inventory_id)
GROUP BY title ORDER BY Count_of_Rented_Movies DESC;

#7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, SUM(p.amount) 
FROM payment p
JOIN staff s ON (p.staff_id=s.staff_id)
GROUP BY store_id;

#7g. Write a query to display for each store its store ID, city, and country.
SELECT store_id, city, country FROM store s
JOIN address a ON (s.address_id=a.address_id)
JOIN city c ON (a.city_id=c.city_id)
JOIN country cntry ON (c.country_id=cntry.country_id);

#7h. List the top five genres in gross revenue in descending order. 
#(Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT c.name AS 'Top Five', SUM(p.amount) AS 'Gross' 
FROM category c
JOIN film_category fc ON (c.category_id=fc.category_id)
JOIN inventory i ON (fc.film_id=i.film_id)
JOIN rental r ON (i.inventory_id=r.inventory_id)
JOIN payment p ON (r.rental_id=p.rental_id)
GROUP BY c.name ORDER BY Gross  LIMIT 5;

#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
#Use the solution from the problem above to create a view. 
#If you haven't solved 7h, you can substitute another query to create a view.
SELECT c.name AS 'Top Five', SUM(p.amount) AS 'Gross' 
FROM category c
JOIN film_category fc ON (c.category_id=fc.category_id)
JOIN inventory i ON (fc.film_id=i.film_id)
JOIN rental r ON (i.inventory_id=r.inventory_id)
JOIN payment p ON (r.rental_id=p.rental_id)
GROUP BY c.name ORDER BY Gross  LIMIT 5;

#8b. How would you display the view that you created in 8a?
SELECT* FROM TopFive;

#8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW TopFive;


select * from film_actor;

