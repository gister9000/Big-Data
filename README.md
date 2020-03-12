# Big Data Science
These are the solutions to exercises from Big Data Science subject from uni. Each folder has test inputs and corresponding correct outputs in text files. To test the code, just pipe in the .in file into the program. Depending on your CPU, it may take a while - some of these algorithms are meant to be performed on high end servers.

## SimHash algo
In computer science, SimHash is a technique for quickly estimating how similar two sets are. The algorithm is used by the Google Crawler to find near duplicate pages. It was created by Moses Charikar.
<br> https://en.wikipedia.org/wiki/SimHash <br></br>

## PCY (aka Apriori algo)
Apriori is an algorithm for frequent item set mining and association rule learning over relational databases. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database. The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends in the database: this has applications in domains such as market basket analysis.
<br> https://en.wikipedia.org/wiki/Apriori_algorithm <br></br>

## DGIM algo
When processing large (possibly infinite) data streams, it's commonly necessary to maintain statistics about the N latest elements. In case of very large N, we can't store N latest elements. In such scenarios, with boolean values coming to the stream, DGIM algorithm estimates the number of ones in N latest elements. Used in search engines.
<br> https://branetheory.org/2014/10/25/dgim-algorithm/ <br></br>

## Collaborative Filtering
Collaborative filtering (CF) is a technique used by recommender systems - it is used to recommend an item to the user based on his activity and activity of similar users. 
<br> https://en.wikipedia.org/wiki/Collaborative_filtering <br></br>

## ClosestBlackNode
Finds a closest black node in the graph.

## NodeRank (aka PageRank)
Search engines have to rank pages somehow. Introducing billions of pages (graph vertices) and trillions of links (graph edges) poses new challenges. PageRank is a method for rating the importance of web pages objectively and mechanically using the link structure of the web. According to Google: "PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites."
<br> https://en.wikipedia.org/wiki/PageRank <br></br>

