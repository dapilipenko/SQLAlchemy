from app import create_app
from appmodels.itemModel import ItemModel
from db import db
from appmodels.storeModel import StoreModel
from appmodels.item_tags import ItemsTags

app = create_app()
with app.app_context():
    db.create_all()
    db.session.query(StoreModel).delete()
    db.session.commit()
    db.session.query(ItemModel).delete()
    db.session.commit()
    items = [
        ItemModel(name="Item 1", price=10.99, store_id=1),
        ItemModel(name="Item 2", price=15.49, store_id=1),
        ItemModel(name="Item 3", price=7.99, store_id=2),
    ]   
    stores = [
        StoreModel(name="Store 1"),
        StoreModel(name="Store 2"),
    ]
    db.session.add_all(stores)
    db.session.commit()
    db.session.add_all(items)
    db.session.commit()
if __name__ == "__main__":
    app.run(debug=True)