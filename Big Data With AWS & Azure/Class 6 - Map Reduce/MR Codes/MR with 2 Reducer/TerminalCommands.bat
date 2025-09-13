# To Compile and Run


# Create new directory for this version
cd /home/mayank0953
mkdir wordcount_two_reducers
cd wordcount_two_reducers

# Create the Java file
vi WordCountTwoReducers.java
# Paste the code above

# Compile
javac -cp $(hadoop classpath) WordCountTwoReducers.java

# Create JAR
jar cf wc_two_reducers.jar WordCount*.class

# Clean previous output if exists
hadoop fs -rm -r /user/mayank0953/output_two_reducers

# Run the job
hadoop jar wc_two_reducers.jar WordCountTwoReducers /user/mayank0953/input/dbzinput.txt /user/mayank0953/output_two_reducers




# To Verify the output


# List files - you should see two part-r-0000* files
hadoop fs -ls /user/mayank0953/output_two_reducers

# View contents of both reducer outputs
hadoop fs -cat /user/mayank0953/output_two_reducers/part-r-00000
hadoop fs -cat /user/mayank0953/output_two_reducers/part-r-00001
