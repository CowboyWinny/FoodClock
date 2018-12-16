CREATE DATABASE foodclock;
CREATE TABLE food( fid serial ,  f_name character(100) ,  calories real ,  proteins real ,  carbs real ,  fats real , food_type character(100));
CREATE TABLE eatevent( eeid serial ,  eventtime time(0) ,  food integer ,  mass real );
CREATE TABLE realeatevent( reeid serial ,  eventtime time(0) ,  food integer ,  mass real );