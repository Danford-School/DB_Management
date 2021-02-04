# DB_Management
CS487 Database Management Systems Implementation 



Part 1: In the beginning, data was created. 

In the following screenshot you can see that we generated new csv files inside our VM. 
https://github.com/Danford-School/DB_Management/blob/main/21.PNG
https://github.com/Danford-School/DB_Management/blob/main/22.PNG

In the following screenshot you can see a sample of the data generated. In this case we only used three of the columns because all of the data together looks unwieldy. 
https://github.com/Danford-School/DB_Management/blob/main/23.PNG

In the following screenshot you can see a sample of all of the data together. As we mentioned, it does look unwieldy, but all of the data is there. 
https://github.com/Danford-School/DB_Management/blob/main/24.PNG


Part 2: README! ME! READ! 
With regards to data generation, we initially started by trying to find a data generator online, as it was permissible to do so. The first data generator we encountered was in Java, however this data generator was creating strings that were far longer than 52 characters. Since this violated the schema of the Wisconsin Benchmark, we moved to a generator that was recommended by the TA. However, after consulting with her, it turned out that this data generator did not produce data for the scalable Wisconsin benchmark. Seeing as we didn’t have much time to spare, Neha was gracious enough to give us a data generator. However, that didn’t feel entirely right, so we decided to try it on our own. We spent many hours reading the Wisconsin benchmark and trying to make a generator that fell within its parameters. Thankfully the convert function, which was the most important function, was already given in the paper in C code so we implemented a python version of that function. Doing this proved quite a bit more difficult than initially expected, for example there was a while loop that was completely throwing our data out of whack. Thankfully, by deleting the while loop we were able to get the appropriate data. We were able to code this out on the vm provided to us because it allowed for pip install of the necessary modules.
We will be working with Postgres because it is a system that we are familiar with due to taking the Intro to Databases course offered at PSU. Also, we feel that it is a very intuitive and user friendly system.
The screen shots presented above demonstrate our ability to load data into the postgres database on our virtual machine in the google cloud.
The lesson we learned was that data generation is a valuable skill in itself. It requires a fair amount of knowledge and experience in coding, to be able to generate the necessary data required to test a database. Furthermore, knowing what data you need to generate and what properties you want to test for are integral to validating the efficacy of a database. The primary issue we encountered during this process was with regards to the data generation. It took a substantial amount of time to make the script work and generate the appropriate data. Mainly, it was the convert function that caused this backlog.
We did not have any issues with the creation of a virtual machine, but that is partially due to two of us being in the Data Engineering course where we did this repeatedly during the first week. Without that experience, I am sure that the creation of the virtual machines would have been more of a trial. 
