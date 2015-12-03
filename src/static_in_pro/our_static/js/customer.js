calculateTotal();
$('.paleblue input').focusout(function(){calculateTotal()});

var selectedProducts = [];
function toggle(source) {
	var value = source.value;
    checkboxes = document.getElementsByName('selection');
    var found = false;
    for(var i = 0; i <= selectedProducts.length; i++){
        if(selectedProducts[i] == value){
        	found = true;
        	selectedProducts.splice(i,1);
        	break;
        }
    }

    if(found == false)
    	selectedProducts.push(value);

    document.getElementById('id_selected_products').value = JSON.stringify(selectedProducts);
}

function selectProducts(){
	document.getElementById('selectProductsForm').submit();
}

function calculateTotal(){
	var totalItems = 0;
	var index = 0;
	var quantities = [];
	$('.paleblue input').each(function () {
		var quantity = this.value;
		quantities.push(parseInt(this.value));
		//update total amount
    	totalItems += parseInt(quantity);
    	index++;
	});
	index = 0;
	var totalPrice = 0;
	$('.product_price').each(function(){
		//get all the product id's. Ignore the header
		if(this.innerHTML[0] != '<'){
			var thisPrice = parseFloat(this.innerHTML).toFixed(2) * quantities[index];
			totalPrice += thisPrice;
			index++;
		}
	})

	$('#totalItems').text(totalItems);
	$('#totalPrice').text(parseFloat(totalPrice).toFixed(2));

}

function updateContains(){
	console.log("update contains");
	var productUpdates = {};
	var productIds = [];
	$('.product_id').each(function(){
		//get all the product id's. Ignore the header
		if(this.innerHTML[0] != '<')
			productIds.push(this.innerHTML);
	})

	index = 0;
	var orderIds = [];
	$('.order_id').each(function(){
		//get all the product id's. Ignore the header
		if(this.innerHTML[0] != '<')
			orderIds.push(this.innerHTML);
	})

	index = 0;
	$('.paleblue input').each(function () {
		var quantity = this.value;
		//update total amount

    	//update the db with the new order quantity
    	productUpdates[index] = [orderIds[index] ,productIds[index] ,quantity];
    	// productUpdates.push({
    	// 	"product_id": productIds[index],
    	// 	 "quantity": quantity
    	// });
    	index++;

	});
	productUpdates["length"] = index;
	document.getElementById('id_update_info').value = JSON.stringify(productUpdates);;
	document.getElementById('updateOrderForm').submit();

}