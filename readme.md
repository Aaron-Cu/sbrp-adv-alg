# **Algorithms for School Bus Route Planning**

## **1\. Greedy Algorithm: Shortest Path First Strategy**

This algorithm constructs bus routes one by one. For each route, it starts at the school and, from its current location, calculates the **true shortest path** to all remaining unvisited stops using Dijkstra's algorithm. It then travels along this path to the closest reachable stop that does not violate the bus's capacity constraint. This process explicitly allows the bus to traverse through already visited nodes if it provides the most efficient path, making it robust for complex road networks. Once a bus is full or no more stops can be reached, the route is completed by finding the shortest path back to the school, and a new route is started.

### **Inputs:**

* **Stops:** A collection of all bus stops, each with properties for location (coordinates) and the number of students to be picked up.
* **School:** The central depot location, which is the start and end point for all routes.
* **CostMatrix:** A data structure, like an adjacency list, that provides the direct travel cost (distance or time) between any two **connected** locations.
* **BusCapacity:** The maximum number of students that a single bus can hold.

### **Output:**

* **Routes:** A list of bus routes, where each route is an ordered sequence of all stops visited (including intermediate traversal stops), beginning and ending at the school.

### **Pseudocode:**

    FUNCTION Greedy_Route_Planner(Stops, School, CostMatrix, BusCapacity)  
        // Initialize a list of all stops that need to be visited.  
        UnvisitedStops = copy(Stops)  
        // This will store the final list of all generated routes.  
        AllRoutes = []

        // Continue creating routes until all stops have been assigned.  
        WHILE UnvisitedStops is not empty
            current_route = [School]
            current_load = 0
            current_location = School
            stops_added_this_route = 0

            LOOP
                // Find the true shortest path from the current location to all other nodes.
                ShortestPaths = find_shortest_path_dijkstra(CostMatrix, current_location)
                
                next_stop = NULL
                min_distance = infinity

                // Iterate through unvisited stops to find the one with the shortest path.
                FOR EACH stop in UnvisitedStops
                    IF (current_load + stop.student_count) <= BusCapacity
                        distance = ShortestPaths.get_distance(stop)
                        IF distance < min_distance
                            min_distance = distance
                            next_stop = stop
                        END IF
                    END IF
                END FOR

                IF next_stop is not NULL
                    stops_added_this_route = stops_added_this_route + 1
                    path_to_next_stop = reconstruct_path(ShortestPaths, next_stop)
                    
                    // Add all intermediate stops from the path to the current route.
                    add path_to_next_stop (excluding start) to current_route
                    
                    current_load = current_load + next_stop.student_count
                    current_location = next_stop
                    remove next_stop from UnvisitedStops
                ELSE
                    BREAK LOOP
                END IF
            END LOOP

            // **Handle disconnected graphs to prevent infinite loops.**
            IF stops_added_this_route == 0 AND UnvisitedStops is not empty
                PRINT "Error: Remaining stops are unreachable."
                BREAK WHILE
            END IF

            // Find and add the shortest path back to the school.
            path_to_school = find_shortest_path_dijkstra(CostMatrix, current_location, School)
            add path_to_school (excluding start) to current_route
            
            add current_route to AllRoutes
        END WHILE

        RETURN AllRoutes 
    END FUNCTION

## **2\. Divide and Conquer: Clustering-Based Routing Algorithm**

This method uses a two-phase approach. First, it divides the problem by grouping bus stops into clusters. Second, it conquers the smaller problems by finding an efficient route within each cluster using a shortest-path-aware heuristic.

### **Phase 1: Cluster Stops**

Group all bus stops into a predefined number of clusters (K) using the k-means algorithm based on their geographical locations.

### **Phase 2: Generate Routes**

For each cluster, generate a route using a **nearest-neighbor heuristic**. This heuristic finds the shortest path (using Dijkstra's algorithm) from the current location to the nearest unvisited stop *within the cluster*, repeating until all stops in the cluster are serviced. The route starts and ends at the school.

### **Inputs:**

* **Stops:** A collection of all bus stops with their location coordinates.
* **School:** The central depot location.
* **K:** The desired number of clusters, which corresponds to the number of buses available.
* **CostMatrix:** The data structure providing travel costs between locations.

### **Output:**

* **Routes:** A set of K routes, one for each cluster.

### **Pseudocode:**

    FUNCTION Clustering_Based_Planner(Stops, School, K, CostMatrix)  
        // PHASE 1: CLUSTER THE STops  
        // Use the k-means algorithm to partition the set of stops into K clusters.  
        Clusters = k_means_clustering(Stops, K)

        AllRoutes = []

        // PHASE 2: GENERATE A ROUTE FOR EACH CLUSTER
        FOR EACH cluster in Clusters
            // Solve for an efficient tour within the cluster.
            tour = solve_tsp_heuristic(cluster, School, CostMatrix)
            add tour to AllRoutes
        END FOR

        RETURN AllRoutes
    END FUNCTION

    FUNCTION solve_tsp_heuristic(ClusterStops, School, CostMatrix)  
        // This heuristic finds a tour, not necessarily the optimal one.  
        Tour = [School]  
        current_location = School  
        UnvisitedInCluster = copy(ClusterStops)

        WHILE UnvisitedInCluster is not empty
            ShortestPaths = find_shortest_path_dijkstra(CostMatrix, current_location)
            next_stop = NULL
            min_distance = infinity

            FOR EACH stop in UnvisitedInCluster
                distance = ShortestPaths.get_distance(stop)
                IF distance < min_distance
                    min_distance = distance
                    next_stop = stop
                END IF
            END FOR
            
            IF next_stop is not NULL
                path_to_next = reconstruct_path(ShortestPaths, next_stop)
                add path_to_next (excluding start) to Tour
                current_location = next_stop
                remove next_stop from UnvisitedInCluster
            ELSE
                BREAK // Cannot reach any more stops in the cluster
            END IF
        END WHILE

        path_to_school = find_shortest_path_dijkstra(CostMatrix, current_location, School)
        add path_to_school (excluding start) to Tour

        RETURN Tour
    END FUNCTION  

## **3. Key Findings & Considerations**

### **Graph Connectivity**

A critical finding during implementation was that the provided real-world data formed a **disconnected graph**. This means there were "islands" of stops with no road connections to the main graph where the school was located. Our final algorithms are robust to this issue: they solve for all reachable stops and then gracefully exit, reporting which stops are unreachable. This prevents infinite loops and correctly identifies data integrity problems.

### **Benchmarking Methodology**

To rigorously compare the two algorithms, a benchmarking process was implemented. For various problem sizes (e.g., 20, 40, 60 stops), the simulation runs multiple trials. In each trial, a random subset of stops is selected from the complete dataset. The **average runtime** and **average total route cost** are then calculated and plotted to provide a reliable comparison of algorithm efficiency (speed) and solution optimality (quality).