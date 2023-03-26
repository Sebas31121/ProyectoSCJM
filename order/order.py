class Order:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        order = self.session['order']
        if not order:
            self.session['order']={}
            self.order=self.session['order']
        else:
            self.order=order 

    def agregar(self,producto):
        id=str(producto.id)
        if id not in self.order.keys():
            self.order[id]={
                "producto_id": producto.id,
                "nombre": producto.name,
                "precio":producto.price,
                "cantidad":1
            }
        else:
            self.order[id]["cantidad"]+1
            self.order[id]["precio"]+=producto.price
        self.guardar_order()
    
    def guardar_order(self):
        self.session["order"]=self.order
        self.session.modified = True

    def eliminar_order(self, producto):
        id=str(producto.id)
        if id in self.order:
            del self.order[id]
            self.guardar_order
    
    def restar(self,producto):
        id=str(producto.id)
        if id in self.order.keys():
            self.order[id]["cantidad"]-=1
            self.order[id]["precio"]-=producto.price
            if self.order[id]["cantidad"]<= 0: self.eliminar_order(producto)
            self.guardar_order()
    
    def limpiar(self):
        self.session['order']={}
        self.session.modified = True