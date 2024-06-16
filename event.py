class Event:
    def __init__(self, id=None, pubkey=None, created_at=None, kind=None, tags=None, content=None, sig=None): #note: tags is a mutable object and re-called each time the contructor is used. So, should not directly set it.
        self.id = id #<32-bytes lowercase hex-encoded sha256 of the serialized event data>, use ""
        self.pubkey = pubkey #use ""
        self.created_at = created_at #number, not string
        self.kind = kind #number, not string
        self.tags = tags or []
        self.content = content #use ""
        self.sig = sig #use ""

    def __repr__(self):
        return f"{{\n  \"id\"={self.id}, \"pubkey\"={self.pubkey}, \"created_at\"={self.created_at}, \"kind\"={self.kind}, \"tags\"={self.tags}, \"content\"={self.content}, \"sig\"={self.sig}"
  
e=Event()
print(e) 
  