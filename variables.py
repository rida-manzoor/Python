#!/usr/bin/env python
# coding: utf-8

# Variable: We can say variables behave like containers which hold some values. Data stored in variables is called value.

# In[2]:


name = "Rida"


# In[3]:


type(name)


# ### Data Types in Python
# >> Numbers:
# This is created by numerical literals, are immutable.
# 1: Boolean
# 2: Integer
# 3: Floating point
# 4: Complex
# 
# >> Sequence:
# is ordered collection of items, where each item is indexed by a integer value. 
# 1: List
# 2: Tuple
# 3: String
# 
# >> Set:
# unorder collection of datatype that is iterable, mutable and has no duplicate value.
# 1: Set(mutable)
# 2: Frozenset(immutable)
# 
# >> Mapping:
# unordered data type in Python. Currently there is only one standard mapping that is dictionary.

# In[5]:


a = range(10)
type(a)


# ### Assigning multiple values to variables in one statement

# In[10]:


a,b,c,d = 2,4,"Hello",0
print("a =",a,"b =",b,"c =",c,"d =",d)


# ### Check data type of varible

# In[14]:


x = 3
print(type(x))

t ="Hello"
print(type(t))

h=7.5
print(type(h))


# ### Check ID of variable
# 
# Every Python object has some ID(memory address) associated with it.
# 
# >Both the variables a and b have same ID, i.e., both a and b are pointing to same memory location.
# 
# >Variables in Python are not actual objects, rather are references to objects that are present in memory.
# 
# >So both the variables a and b are refering to same object 10 in memory and thus having the same ID.

# In[18]:


u=3
print(id(u))
k=2
print(id(k))


# In[19]:


a=3
b=3
id(a),id(b)


# In[20]:


h ="Hello"
id(h)


# In[21]:


h="World"
id(h)


# Note that the string object "Hello" has become an orphaned object, as no variable is refering to it now. This is because the reference h is now pointing/referring to a new object "World". All orphan objects are reaped by Python garbage collector.
# 
# 
