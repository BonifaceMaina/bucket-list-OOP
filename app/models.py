
users={'username':'password'}
bucketlistdict={} 
items={} 
i = 0
j = 0

class User(object):
    """User"""  

    def CreateUsers(self, username, password):
        """Registering new users"""
        if users.get(username):
            return "Username in use"
        else:
            users[username] = password
        return "Registered"     

    
    def Login(self, username, password):
        if users.get(username):
            if users[username] == password:
                return "Logged in successfully"
            return "Wrong Password"
        return "You are not registered"

class Bucketlist(object):
    """Creating, deleting, Editing Bucketlists"""
    def CreateBucketList(self, bucket):
        global i

        if bucket =='':
            return "No empty items allowed"
        elif bucket in bucketlistdict.values():
            return "That bucketlist exists"        
        else:
            i += 1
            bucketlistdict.update({i : bucket})
            return "Added bucketlist"

    def ShowBucketLists(self):
        return bucketlistdict

    def EditBucketList(self, key, value):
        if key in bucketlistdict:
            bucketlistdict[key] = value
            return "Edit successful"

    def DeleteBucketLists(self, key):
        if key in bucketlistdict:
            del bucketlistdict[key]
            return "Deleted Item"


class Items(object):
    """the CRUD for a bucketlist"""
    def CreateItems(self, item):
        global j
        if item =='':
            return "No empty items allowed"
        elif item in items.values():
            return "Already Exists"
        else:
            j += 1
            items.update({j : item})
            return "Item added"

    def ShowItems(self):
        return items

    def EditItems(self, key, value):
        if key in items:
            items[key] = value
            return "Edit Successful"

    def DeleteItems(self, key):
        if key in items:
            del items[key]
            return "Item deleted"
