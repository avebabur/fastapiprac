from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from fastapi import APIRouter, Header, Cookie, Form
from typing import Optional, List


router = APIRouter(
    prefix='/product',
    tags=['product']
)


products = ['watch', 'camera', 'phone']

@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products

@router.get('/all')
def get_all_products():
    # return products
    data = " ".join(products)
    response = Response(content=data, media_type='text/plain')
    response.set_cookie(key='test_cookie', value='test_cookie_value')
    return response

@router.get('/withheader')
def get_products(response: Response, custom_header: Optional[list[str]] = Header(None), test_cookie: Optional[str] = Cookie(None)):
    if custom_header:
        response.headers['custom-response-header'] = " and ".join(custom_header)
    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }

@router.get('/{product_id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            },
        },
        "description": "Returns the HTML for the product"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not found"
            },
        },
        "description": "A clear message that the product was not found"

    },
})
def get_product(product_id: int):
    if id > len(products):
        out = "Product not found"
        return PlainTextResponse(status_code=404, content=out, media_type='text/plain')
    else:
        product = products[product_id]
        out = f"""
        <head>
            <style>
                .product {{
                    with: 500px;
                    height: 30px;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center;
                }}
            </style>
        </head>
        <div class="product">
            {product}
        </div>

        """
        return HTMLResponse(content=out, media_type='text/html')