from flask import Flask, jsonify,request
from products import products

app = Flask(__name__)

#metodos get=obtener datos post=guardar datos put=editar datos delete=borrar datos

@app.route("/")
def index():
    return jsonify(products)

@app.route('/productos')
def getProductos():
    return jsonify({'Productos':products,'Menssage': 'Elemento Ubicado'})

@app.route('/productos/<string:item>')
def recepcion_producto(item):
    #busca el elemento product 
    objetoEncontrado = [busqueda for busqueda in products if busqueda['nombre'] == item]
    #productsFound = [product for product in products if product['nombre'] == item]
    if (len(objetoEncontrado) > 0):
        return jsonify({'Producto':objetoEncontrado[0]})
    return jsonify({'Mensaje':'Producto no encontrado'})

@app.route('/productos',methods=['POST'])
def addProduct():
    newProduct ={
        'nombre':request.json['nombre'],
        'precio':request.json['precio'],
        'unidades':request.json['unidades']
    }
    products.append(newProduct)
    return jsonify({'Mensaje':'Datos recibidos Exitosamente','datos':products})

@app.route('/productos/<string:objEdit>',methods=['PUT'])
def editProduct(objEdit):
    elementoAgregar = [objetivo for objetivo in products if objetivo['nombre'] == objEdit]
    if(len(elementoAgregar) > 0):
        elementoAgregar[0]['nombre'] = request.json['nombre']
        elementoAgregar[0]['precio'] = request.json['precio']
        elementoAgregar[0]['unidades'] = request.json['unidades']
        return jsonify({'Accion':'Accion exitosa','Datos actualizados': elementoAgregar[0]})
    return jsonify({'Accion':'Fallida'})

@app.route('/productos/<string:elemBorrar>', methods=['DELETE'])
def delProduct(elemBorrar):
    itemBorrar = [item for item in products if item['nombre'] == elemBorrar]
    if len(itemBorrar) > 0:
        products.remove(itemBorrar[0])
        return jsonify({'Mensaje':'borrado exitoso','Datos': products})
    return jsonify({'Mensaje':'Operacion fallida'})

if __name__ == '__main__':
    app.run(debug = True, port=4001)

