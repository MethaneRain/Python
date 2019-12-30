# Tips-Tricks

### Over the years I've been able to collect various tips and tricks of the trade that have helped me along the way in Python. To help find these quickly I've documented them here. 

### 
----

Passing variables as strings:

```Python
a = 'these'
b = 'are positional'
c = ''.join(['py','th','on',' ','va','ri','ab','le','s']) + '!'

%%bash -s "$a" "$b" "$c"
echo "a=$1 b=$2 c=$3"

>>>
a=these b=are positional c=python variables!
```
