Запуск
======

#. Скопировать файлы mapper.py, reducer.py, sentences.txt на машину с Hadoop.
#. Скопировать эти файлы в HDFS

    ::

        cd /usr/local/hadoop
        bin/hadoop dfs -copyFromLocal /tmp/mapper.py /tmp/mapper.py
        bin/hadoop dfs -copyFromLocal /tmp/reducer.py /tmp/reducer.py
        bin/hadoop dfs -copyFromLocal /tmp/sentences.txt /tmp/sentences.txt

#. Назначить права на исполнение

    ::

        bin/hadoop dfs -chmod +x /tmp/mapper.py
        bin/hadoop dfs -chmod +x /tmp/reducer.py

#. Запустить вычисления

    ::

    bin/hadoop jar /usr/local/hadoop-2.4.1/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
    -file /tmp/mapper.py -mapper mapper.py \
    -file /tmp/reducer.py  -reducer reducer.py \
    -input /tmp/sentences.txt \
    -output /tmp/answer

