# Create input directory if not exists
hadoop fs -mkdir -p /user/mayank0953/input_large

# Copy the large log file to HDFS
hadoop fs -put /home/mayank0953/logfile.txt /user/mayank0953/input_large/



# Single Reducer Run 

# Clean previous output
hadoop fs -rm -r /user/mayank0953/output_single_large

# Run the job
hadoop jar /home/mayank0953/wordcount/wc.jar WordCount /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_single_large

# View result
hadoop fs -ls /user/mayank0953/output_single_large
hadoop fs -cat /user/mayank0953/output_single_large/part-r-00000



# Two Reducer Run

# Clean previous output
hadoop fs -rm -r /user/mayank0953/output_two_large

# Run the job
hadoop jar /home/mayank0953/wordcount_two_reducers/wc_two_reducers.jar WordCountTwoReducers /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_two_large

# View results (two files)
hadoop fs -ls /user/mayank0953/output_two_large
hadoop fs -cat /user/mayank0953/output_two_large/part-r-00000
hadoop fs -cat /user/mayank0953/output_two_large/part-r-00001




# No Reducer Run

# Clean previous output
hadoop fs -rm -r /user/mayank0953/output_no_reducer_large

# Run the job
hadoop jar /home/mayank0953/wordcount_no_reducer/wc_no_reducer.jar WordCountNoReducer /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_no_reducer_large

# View results (multiple mapper files)
hadoop fs -ls /user/mayank0953/output_no_reducer_large
hadoop fs -cat /user/mayank0953/output_no_reducer_large/part-m-*



# To compare execution Time

# For single reducer
time hadoop jar /home/mayank0953/wordcount/wc.jar WordCount /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_single_large

# For two reducers
time hadoop jar /home/mayank0953/wordcount_two_reducers/wc_two_reducers.jar WordCountTwoReducers /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_two_large

# For no reducer
time hadoop jar /home/mayank0953/wordcount_no_reducer/wc_no_reducer.jar WordCountNoReducer /user/mayank0953/input_large/logfile.txt /user/mayank0953/output_no_reducer_large




# Access the Hadoop web interface through your browser
# Usually available at master_node:8088

# Or use command line
mapred job -list

# To see detailed job status
mapred job -status job_id