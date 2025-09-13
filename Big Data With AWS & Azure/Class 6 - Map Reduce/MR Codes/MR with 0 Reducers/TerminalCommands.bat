# Create new directory for this version
cd /home/mayank0953
mkdir wordcount_no_reducer
cd wordcount_no_reducer

# Create the Java file
vi WordCountNoReducer.java
# Paste the code above

# Compile
javac -cp $(hadoop classpath) WordCountNoReducer.java

# Create JAR
jar cf wc_no_reducer.jar WordCount*.class

# Clean previous output if exists
hadoop fs -rm -r /user/mayank0953/output_no_reducer

# Run the job
hadoop jar wc_no_reducer.jar WordCountNoReducer /user/mayank0953/input/dbzinput.txt /user/mayank0953/output_no_reducer












# List files - you should see part-m-* files (mapper output)
hadoop fs -ls /user/mayank0953/output_no_reducer

# View the output
hadoop fs -cat /user/mayank0953/output_no_reducer/part-m-*