'''
Phone List
Given a list of phone numbers, determine if it is consistent in the sense that no number is the 
prefix of another. Let’s say the phone catalogue listed these numbers:

Emergency 911
Alice 97 625 999
Bob 91 12 54 26

In this case, it’s not possible to call Bob, because the central would direct your call to the 
emergency line as soon as you had dialled the first three digits of Bob’s phone number. 
So this list would not be consistent.

Input

The first line of input gives a single integer, 1 <= t <= 40, the number of test cases. 
Each test case starts with n, the number of phone numbers, on a separate line, 1 <= n <= 10000. 
Then follows n lines with one unique phone number on each line. A phone number is a sequence of at most ten digits.

Output

For each test case, output “YES” if the list is consistent, or “NO” otherwise.

Example

Input:
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

Output:
NO
YES
'''

'''
The hypermajority of solutions on spoj.com are run in C++ because people conclude that Python is too slow.
Here is an example of a working C++ template. There's an opportunity to study solutions with a coach at 
codementor. 

#include<bits/stdc++.h>
			using namespace std;
			#define pb push_back
			#define mp make_pair
			#define nline cout<<"\n"
			#define fast ios_base::sync_with_stdio(false),cin.tie(0)
			#define ain(A, B, C) assert(IN(A, B, C))
			#define ull unsigned long long int
			#define ll long long int
			#define pii pair<int,int>
			#define MAXX 100009
			#define fr(a,b,i) for(int i=a;i<b;i++)
			vector<int>G[MAXX];
			struct node
			{
				bool leaf;
				struct node* child[10];
				node()
				{
					for(int i=0;i<10;i++)child[i]=NULL;
					leaf=false;
				}
			};
			struct node* root;
			bool add(string &s)
			{
				struct node* curr=root;
				bool result = false;
				for(int i=0;i<s.length();i++)
				{
					if (curr->leaf) {
						result = true;
					}
					int SS=s[i]-'0';
					if(curr->child[SS]==NULL)
						curr->child[SS]=new node();
					curr=curr->child[SS];
				}
				for(int i=0;i<10;i++)
			   {
			   	if(curr->child[i]!=NULL)
			   	  return true;
			   }
 
			   if (curr->leaf || result) {
			   	return true;
			   }
 
				curr->leaf=true;
				return false;
			}
			void deleteme(node* curr)
			{
				for(int i=0;i<10;i++)
				 if(curr->child[i])
				  deleteme(curr->child[i]);
				delete curr;
			}
			int main()
			{
				fast;
			   int t;
			   cin>>t;
			   while(t--)
			   {
			   	root=new node();
			   	int n,f=0;
			   	cin>>n;
			   	for(int i=0;i<n;i++)
			   	{
			   		string s;
			   		cin>>s;
			   		if(add(s)){f=1;}
			   	}
			   	if(f)
			   	cout<<"NO"<<endl;
			   	else
			   	cout<<"YES"<<endl;
			    	deleteme(root);
			   }
			   return 0;
			}

source guidance credit to Vamsi Sangam
'''




#the solution below is unfotunately too slow

class Trie:
    def __init__(self):
        self.childs = [None] * 10
        self.isLeaf = False

def insertInTrie(trie, string):
    for i in range(len(string)):
        cur = int(string[i])
        if trie.childs[cur] is None:
            temp = Trie()
            trie.childs[cur] = temp
        trie = trie.childs[cur]
        if trie.isLeaf:
            return False
    trie.isLeaf = True
    return True

t = int(input())
while t > 0:
    n = int(input())
    vec = []
    for i in range(n):
        vec.append(input())
    vec.sort()
    canInsert = True
    trie = Trie()
    for i in range(n):
        res = insertInTrie(trie, vec[i])
        if not res:
            canInsert = False
            break
    if canInsert:
        print("YES")
    else:
        print("NO")
    t -= 1

'''
Key concepts:
-how to use break and -=-1 to code for various outcomes in a while loop
-creating a trie and checking whether new inputs are existing leaves within the trie
-creating a class object/ data structure and initializing it
'''

'''
source guidance credit to love1024
'''
