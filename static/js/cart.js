let btns = document.getElementsByClassName('addtocart')
for(let i=0;i<btns.length;i++){
    btns[i].addEventListener('click',function(){
        let productId = this.dataset.product
        let action=this.dataset.action
        console.log(productId)
        location.reload()
        
        if(user==="AnonymousUser"){
            console.log("User not logged in")
        }
        else{
            updateCart(productId,action)
        }
    })
}
function updateCart(id,action){
    let url="/updatecart/"
    fetch(url,{
        method:'POST',
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken,
        },
        body:JSON.stringify({"productId":id,"action":action})
    })
    .then(response=>response.json())
    .then(data=>console.log(data))
}

let quantityField=document.getElementsByClassName('quantity')
for(let i=0;i<quantityField.length;i++){
    quantityField[i].addEventListener('change',function(){
        let quantityFieldValue= quantityField[i].value
        let quantityFieldProduct=quantityField[i].parentElement.parentElement.parentElement.children[1].children[0].innerText
        //console.log(quantityFieldProduct)
        location.reload()
        let url="/updatequantity/"
        fetch(url,{
            method:"POST",
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken
            },
            body:JSON.stringify({"qfv":quantityFieldValue,"qfp":quantityFieldProduct,})   
        })
        .then(response=>response.json())
        .then(data=>console.log(data))
    })
}

$(".delete-product").on("click",function(){
    let product_id=$(this).attr("data-product")
    let this_val=$(this)
    //console.log(product_id) 
    deleteProduct(product_id)
    location.reload()

})
function deleteProduct(product_id){
    let url="/deleteProduct/"
    fetch(url,{
        method:'POST',
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken,
        },
        body:JSON.stringify({"product_id":product_id})
    })
    .then(response=>response.json())
    .then(data=>console.log(data))
    
}