##### Automatic changing ip (or high bytes in ip) in the set of dns-files.  
The script `ip_replace.py` changes ip (or high bytes in ip) in the set of dns files.  

In the head of the script you need to change this data.  
For example:   

	replace_list=[
					# domain	old high bytes  new high bytes
		        ['example1.com','10.10.10.',	'10.10.11.'],
		        ['example2.com','12.12.10.',	'12.12.11.'],

            ]

##### How it works
1. Create empty directories `old`  and `new` in the directory with a script.  
2. Put in the directory `old` dns-files (with .db)  
For example: 

		example1.com.db  
		example2.com.db  

3. Change `replace_list` In the head of the script.    
4. In the directory `new` will create new dns-files with new ips.   

##### Usage
		python ip_replace.py

It works without any additional packages dependencies.

