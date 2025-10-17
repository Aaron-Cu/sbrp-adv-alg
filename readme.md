# **Algorithms for School Bus Route Planning**

## **1\. Greedy Algorithm: Shortest Path First Strategy**

This algorithm constructs bus routes one by one. For each route, it starts at the school and, from its current location, calculates the shortest path to all remaining unvisited stops. It then travels to the closest reachable stop that does not violate the bus's capacity constraint. This process allows the bus to traverse through already visited nodes if it provides the most efficient path. Once a bus is full or no more stops can be reached, the route is completed by finding the shortest path back to the school, and a new route is started.

### **Inputs:**

* **Stops:** A collection of all bus stops, each with properties for location (coordinates) and the number of students to be picked up.  
* **School:** The central depot location, which is the start and end point for all routes.  
* **CostMatrix:** A data structure, like an adjacency list, that provides the direct travel cost (distance or time) between any two connected locations.  
* **BusCapacity:** The maximum number of students that a single bus can hold.

### **Output:**

* **Routes:** A list of bus routes, where each route is an ordered sequence of all stops visited, beginning and ending at the school.

### **Pseudocode:**

    FUNCTION Greedy\_Route\_Planner(Stops, School, CostMatrix, BusCapacity)  
        // Initialize a list of all stops that need to be visited.  
        UnvisitedStops \= copy(Stops)  
        // This will store the final list of all generated routes.  
        AllRoutes \= \[\]

        // Continue creating routes until all stops have been assigned.  
        WHILE UnvisitedStops is not empty  
            // Start a new route from the school.  
            current\_route \= \[School\]  
            current\_load \= 0  
            current\_location \= School

            // Loop to add stops to the current route.  
            LOOP  
                // Find the true shortest path from the current location to all other nodes.  
                ShortestPaths \= find\_shortest\_path\_dijkstra(CostMatrix, current\_location)  
                
                // Find the best candidate stop to add next.  
                next\_stop \= NULL  
                min\_distance \= infinity

                // Iterate through all remaining unvisited stops.  
                FOR EACH stop in UnvisitedStops  
                    // Check if adding this stop exceeds the bus capacity.  
                    IF (current\_load \+ stop.student\_count) \<= BusCapacity  
                        // Get the shortest path distance to this stop.  
                        distance \= ShortestPaths.get\_distance(stop)  
                        IF distance \< min\_distance  
                            min\_distance \= distance  
                            next\_stop \= stop  
                        END IF  
                    END IF  
                END FOR

                // If a valid next stop was found, add its full path to the route.  
                IF next\_stop is not NULL  
                    // Reconstruct the sequence of stops to get to the next\_stop.  
                    path\_to\_next\_stop \= reconstruct\_path(ShortestPaths, next\_stop)  
                    
                    // Add all intermediate stops from the path to the current route.  
                    add path\_to\_next\_stop (excluding start) to current\_route  
                    
                    current\_load \= current\_load \+ next\_stop.student\_count  
                    current\_location \= next\_stop  
                    remove next\_stop from UnvisitedStops  
                ELSE  
                    // If no more stops can be added, end this route.  
                    BREAK LOOP  
                END IF  
            END LOOP

            // Find the shortest path back to the school and complete the route.  
            path\_to\_school \= find\_shortest\_path\_dijkstra(CostMatrix, current\_location, School)  
            add path\_to\_school (excluding start) to current\_route  
            
            // Add the completed route to our list of all routes.  
            add current\_route to AllRoutes  
        END WHILE

        RETURN AllRoutes  
    END FUNCTION

## **2\. Divide and Conquer: Clustering-Based Routing Algorithm**

This method uses a two-phase approach. First, it divides the problem by grouping bus stops into clusters. Second, it conquers the smaller problems by finding an efficient route within each cluster using a shortest-path-aware heuristic.

### **Phase 1: Cluster Stops**

Group all bus stops into a predefined number of clusters (K) using the k-means algorithm based on their geographical locations.

### **Phase 2: Generate Routes**

For each cluster, generate a route using a nearest-neighbor heuristic. This heuristic finds the shortest path (using Dijkstra's algorithm) from the current location to the nearest unvisited stop within the cluster, repeating until all stops in the cluster are serviced. The route starts and ends at the school.

### **Inputs:**

* **Stops:** A collection of all bus stops with their location coordinates.  
* **School:** The central depot location.  
* **K:** The desired number of clusters, which corresponds to the number of buses available.  
* **CostMatrix:** The data structure providing travel costs between locations.

### **Output:**

* **Routes:** A set of K optimized routes, one for each cluster.

### **Pseudocode:**

    FUNCTION Clustering\_Based\_Planner(Stops, School, K, CostMatrix)  
        // PHASE 1: CLUSTER THE STops  
        // Use the k-means algorithm to partition the set of stops into K clusters.  
        Clusters \= k\_means\_clustering(Stops, K)

        AllRoutes \= \[\]

        // PHASE 2: GENERATE A ROUTE FOR EACH CLUSTER  
        FOR EACH cluster in Clusters  
            // Solve for the best tour within the cluster using a shortest-path heuristic.  
            optimal\_tour \= solve\_tsp\_heuristic(cluster, School, CostMatrix)  
            add optimal\_tour to AllRoutes  
        END FOR

        RETURN AllRoutes  
    END FUNCTION

    FUNCTION solve\_tsp\_heuristic(ClusterStops, School, CostMatrix)  
        // This heuristic finds a tour, not necessarily the optimal one.  
        Tour \= \[School\]  
        current\_location \= School  
        UnvisitedInCluster \= copy(ClusterStops)

        WHILE UnvisitedInCluster is not empty  
            // Find shortest paths from the current location to all other nodes.  
            ShortestPaths \= find\_shortest\_path\_dijkstra(CostMatrix, current\_location)  
            
            next\_stop \= NULL  
            min\_distance \= infinity

            // Find the nearest unvisited stop in the current cluster.  
            FOR EACH stop in UnvisitedInCluster  
                distance \= ShortestPaths.get\_distance(stop)  
                IF distance \< min\_distance  
                    min\_distance \= distance  
                    next\_stop \= stop  
                END IF  
            END FOR  
            
            // If a path is found, add it to the tour.  
            IF next\_stop is not NULL  
                path\_to\_next \= reconstruct\_path(ShortestPaths, next\_stop)  
                add path\_to\_next (excluding start) to Tour  
                current\_location \= next\_stop  
                remove next\_stop from UnvisitedInCluster  
            ELSE  
                BREAK // Cannot reach any more stops in the cluster  
            END IF  
        END WHILE

        // Find the shortest path back to the school to complete the tour.  
        path\_to\_school \= find\_shortest\_path\_dijkstra(CostMatrix, current\_location, School)  
        add path\_to\_school (excluding start) to Tour  
        
        RETURN Tour  
    END FUNCTION  
