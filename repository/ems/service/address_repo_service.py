from sqlalchemy.orm import Session
from repository.ems.model.ems import Address


class AddressRepoService:
    def save(address : Address, db : Session):
        db.query(Address).filter(Address.eid == address.eid).update({Address.is_primary : False})
        db.add(address)
        db.commit()
    
    def update(address : Address, db : Session):
        db.query(Address).filter(Address.id == address.id, Address.eid == address.eid).update({
                                      Address.first_line : address.first_line,
                                      Address.second_line : address.second_line,
                                      Address.land_mark : address.land_mark,
                                      Address.phone : address.phone,
                                      Address.pincode : address.pincode,
                                      Address.city : address.city,
                                      Address.state : address.state
                                      })
        db.commit()

    
    def getByIdAndEid(id : int, eid : int,  db : Session):
        return db.query(Address).filter(Address.id == id, Address.eid == eid).first()
    
    def getByEid(eid : int,  db : Session):
        return db.query(Address).filter(Address.eid == eid).all()
    
    
    def makePrimary(id : int, eid : int, db : Session):
        db.query(Address).filter(Address.eid == eid).update({Address.is_primary : False})
        db.commit()
        db.query(Address).filter(Address.id == id, Address.eid == eid).update({Address.is_primary : True})
        db.commit()
    
    def deleteByIdAndEid(id: int, eid, db : Session):
        db.query(Address).filter(Address.id == id, Address.eid == eid).delete()
        db.commit()