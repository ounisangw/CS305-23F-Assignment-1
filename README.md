# CS305-23F-Assignment-1
This is a repository for Programming Assignment 1 in SUSTech CS305, Computer Network course.

If you have any problem about this assignment, you are welcomed to raise an issue anytime!

Hope you can ENJOY your programming! <3



#### Update：

2023.10.19 

Modify some requires in POP3 server: For command RETR, it requies a specific parameter as the message number to retrieve. (e.g. RETR 1)



2023.10.26

Simple test scripts released for students to do self-checking. Here is a tutorial for usage:

① Use cmd under the **project directory** (default: .../assign1/src) and type command:

```
pip install -r requirements.txt
```

② Move your "server.py" to same directory as "test.py"(.../as1-benchmark-release).

③ Use you cmd to run:

```
python test.py
```

for running all the test cases together, and

```
python test.py -f X
```

'**X**' here should be replaced by the index of the specific test case you want to run individually. There is no need for you to additionally run servers. The test script will pull up the server it needs itself, and shut it down when finish testing.

④ All the test cases are put in the 'fixtures' folder. Feel free to inspect them or add your own cases for test imitating the cases given. These cases cover a lot of pts, but may not be completely consistent with the sample we will ultimately use for testing. (May be 90% similar?/thinking)

Again, we will **NOT cover any (corner) case** that are not mentioned in the Assignment Document. Its quite easy for you to get through the test as if the MOST basic work is done.

Hope you have fun programming in CS305 class! 



2023.10.26

Test scrpits fixed. What is worth mentioning is that:

* All the tests about POP3 are based on SMTP tests. That is to say, only if you have passed all the tests related to SMTP can you possibly pass the POP3 test. If you failed with finishing some implementations of SMTP which causes you failed to pass all POP3 tests, but you think you have implemented some functions of POP3, **prove it** (with screen shot etc.) in your final report.
* For the screenshot of Wireshark, you just need to show your result of capturing the **SMTP AND POP3** packets when running test case "**4.yml**". 

* You are suggested to run the tests under **Linux** environment.



2023.10.27

Fix test case 7.yml
