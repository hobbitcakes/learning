val pairs = sc.parallelize(List(("a", 1), ("a", 5), ("b", 6), ("b", 3), ("c", 2)))

val results = pairs.reduceByKey((a,b) => { a > b match {case true => a case false => b}}).collectAsMap()
