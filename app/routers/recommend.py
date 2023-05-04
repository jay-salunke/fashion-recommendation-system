
from typing import Annotated
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from routers.auth import get_current_user
from databases import schemas, crud
import boto3

import os
from databases.getdb import get_db
from databases import crud

router = APIRouter(prefix="/recommend")
# get access key and secret key from environment variables

# personalizeRt = boto3.client('personalize-runtime',
#                              aws_access_key_id=os.environ.get('access_key'),
#                              aws_secret_access_key=os.environ.get(
#                                  'secret_key'),
#                              region_name='ap-south-1')


@router.post("/bestseller")
def bestseller(user=Depends(get_current_user), db: Session = Depends(get_db)):
    # response = personalizeRt.get_recommendations(
    #     recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/best',
    #     userId=user.user_id,
    #     numResults=10
    # )
    # data = response['itemList']
    # lis = []
    # for i in range(0, len(data)):
    #     lis.append(data[i]['itemId'])
    # result = crud.get_items_by_item_id(db=db, item_ids=lis)

    # return result
    return [
    {
        "item_id": 456163086,
        "product_name": "Woody(1)",
        "product_group_name": "Garment Upper body",
        "colour_group_code": 93,
        "index_code": "A",
        "section_no": 16,
        "description": "Wide top in sweatshirt fabric with a lined drawstring hood, kangaroo pocket and ribbing at the cuffs and hem.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 308,
        "department_no": 1676,
        "index_group_no": 1,
        "garment_group_no": 1002,
        "price": "0.0338813559322033"
    },
    {
        "item_id": 547780003,
        "product_name": "Basic sweatpants",
        "product_group_name": "Garment Lower body",
        "colour_group_code": 7,
        "index_code": "D",
        "section_no": 51,
        "description": "Trousers in soft sweatshirt fabric with an elasticated drawstring waist, side pockets and ribbed hems. Soft brushed inside.",
        "graphical_appearance_no": 1010010,
        "product_type_no": 272,
        "department_no": 1643,
        "index_group_no": 2,
        "garment_group_no": 1002,
        "price": "0.022864406779661"
    },
    {
        "item_id": 715624001,
        "product_name": "Becka hoodie",
        "product_group_name": "Garment Upper body",
        "colour_group_code": 9,
        "index_code": "D",
        "section_no": 51,
        "description": "Long-sleeved top in soft sweatshirt fabric with a jersey-lined, drawstring hood, kangaroo pocket and ribbing at the cuffs and hem. Soft brushed inside.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 308,
        "department_no": 1643,
        "index_group_no": 2,
        "garment_group_no": 1002,
        "price": "0.0254067796610169"
    },
    {
        "item_id": 720125001,
        "product_name": "SUPREME RW tights",
        "product_group_name": "Garment Lower body",
        "colour_group_code": 9,
        "index_code": "S",
        "section_no": 5,
        "description": "Sports tights in fast-drying functional fabric with a wide waistband to hold in and shape the waist. Regular waist with a concealed key pocket in the waistband.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 273,
        "department_no": 8310,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0338813559322033"
    },
    {
        "item_id": 740922001,
        "product_name": "Veronica seamless bra",
        "product_group_name": "Garment Upper body",
        "colour_group_code": 9,
        "index_code": "S",
        "section_no": 5,
        "description": "Fully lined sports bra in fast-drying functional fabric. Lightly padded cups with removable inserts, adjustable shoulder straps and a racer back. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
        "graphical_appearance_no": 1010010,
        "product_type_no": 254,
        "department_no": 8316,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0254067796610169"
    },
    {
        "item_id": 757303014,
        "product_name": "HONEY seamless bra (1)",
        "product_group_name": "Underwear",
        "colour_group_code": 6,
        "index_code": "S",
        "section_no": 5,
        "description": "Sports bra in fast-drying functional fabric with jacquard-patterned details, removable inserts, adjustable shoulder straps that cross at the back and wide ribbing at the hem. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 306,
        "department_no": 8316,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0304915254237288"
    },
    {
        "item_id": 759871002,
        "product_name": "Tilda tank",
        "product_group_name": "Garment Upper body",
        "colour_group_code": 9,
        "index_code": "D",
        "section_no": 80,
        "description": "Cropped, fitted top in cotton jersey with narrow shoulder straps.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 253,
        "department_no": 3936,
        "index_group_no": 2,
        "garment_group_no": 1002,
        "price": "0.0050677966101694"
    },
    {
        "item_id": 791587015,
        "product_name": "Speedy conscious tee",
        "product_group_name": "Garment Upper body",
        "colour_group_code": 92,
        "index_code": "S",
        "section_no": 5,
        "description": "Straight-cut sports top in fast-drying mesh with short sleeves and a rounded hem. Slightly longer at the back. The polyester content of the top is recycled.",
        "graphical_appearance_no": 1010016,
        "product_type_no": 255,
        "department_no": 8316,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0254067796610169"
    },
    {
        "item_id": 852584001,
        "product_name": "SUPREME RW tights",
        "product_group_name": "Unknown",
        "colour_group_code": 9,
        "index_code": "S",
        "section_no": 5,
        "description": "High-waisted, ankle-length sports tights in fast-drying functional fabric. Wide panel to hold in and shape the waist. Concealed key pocket in the waistband.",
        "graphical_appearance_no": 1010016,
        "product_type_no": -1,
        "department_no": 8310,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0338813559322033"
    },
    {
        "item_id": 918292001,
        "product_name": "STRONG HW seamless tights",
        "product_group_name": "Garment Lower body",
        "colour_group_code": 9,
        "index_code": "S",
        "section_no": 5,
        "description": "Sports tights in fast-drying functional fabric with jacquard-patterned details. High waist with wide, elasticated ribbing. The tights are designed with the minimum number of seams for a more comfortable fit and increased mobility.",
        "graphical_appearance_no": 1010010,
        "product_type_no": 273,
        "department_no": 8310,
        "index_group_no": 26,
        "garment_group_no": 1005,
        "price": "0.0397966101694915"
    }
]


@router.post("/freq")
def frequently_bought_toghether(user=Depends(get_current_user), db: Session = Depends(get_db)):
    # transaction = crud.get_transactions_for_item(db=db, user_id=user.user_id)
    # if transaction:
    #     if transaction.item_id:
    #         response = personalizeRt.get_recommendations(
    #             recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/frequently',
    #             itemId=str(transaction.item_id),
    #             numResults=10
    #         )
    #         data = response['itemList']
    #         lis = []
    #         for i in range(0, len(data)):
    #             lis.append(data[i]['itemId'])
    #         result = crud.get_items_by_item_id(db=db, item_ids=lis)

    #         return result
    # return "None"
    return [
        {
            "item_id": 456163086,
            "product_name": "Woody(1)",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 93,
            "index_code": "A",
            "section_no": 16,
            "description": "Wide top in sweatshirt fabric with a lined drawstring hood, kangaroo pocket and ribbing at the cuffs and hem.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 308,
            "department_no": 1676,
            "index_group_no": 1,
            "garment_group_no": 1002,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 547780003,
            "product_name": "Basic sweatpants",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 7,
            "index_code": "D",
            "section_no": 51,
            "description": "Trousers in soft sweatshirt fabric with an elasticated drawstring waist, side pockets and ribbed hems. Soft brushed inside.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 272,
            "department_no": 1643,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.022864406779661"
        },
        {
            "item_id": 715624001,
            "product_name": "Becka hoodie",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "D",
            "section_no": 51,
            "description": "Long-sleeved top in soft sweatshirt fabric with a jersey-lined, drawstring hood, kangaroo pocket and ribbing at the cuffs and hem. Soft brushed inside.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 308,
            "department_no": 1643,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 720125001,
            "product_name": "SUPREME RW tights",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports tights in fast-drying functional fabric with a wide waistband to hold in and shape the waist. Regular waist with a concealed key pocket in the waistband.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 273,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 740922001,
            "product_name": "Veronica seamless bra",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Fully lined sports bra in fast-drying functional fabric. Lightly padded cups with removable inserts, adjustable shoulder straps and a racer back. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 254,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 757303014,
            "product_name": "HONEY seamless bra (1)",
            "product_group_name": "Underwear",
            "colour_group_code": 6,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports bra in fast-drying functional fabric with jacquard-patterned details, removable inserts, adjustable shoulder straps that cross at the back and wide ribbing at the hem. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 306,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0304915254237288"
        },
        {
            "item_id": 759871002,
            "product_name": "Tilda tank",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "D",
            "section_no": 80,
            "description": "Cropped, fitted top in cotton jersey with narrow shoulder straps.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 253,
            "department_no": 3936,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.0050677966101694"
        },
        {
            "item_id": 791587015,
            "product_name": "Speedy conscious tee",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 92,
            "index_code": "S",
            "section_no": 5,
            "description": "Straight-cut sports top in fast-drying mesh with short sleeves and a rounded hem. Slightly longer at the back. The polyester content of the top is recycled.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 255,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 852584001,
            "product_name": "SUPREME RW tights",
            "product_group_name": "Unknown",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "High-waisted, ankle-length sports tights in fast-drying functional fabric. Wide panel to hold in and shape the waist. Concealed key pocket in the waistband.",
            "graphical_appearance_no": 1010016,
            "product_type_no": -1,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 918292001,
            "product_name": "STRONG HW seamless tights",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports tights in fast-drying functional fabric with jacquard-patterned details. High waist with wide, elasticated ribbing. The tights are designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 273,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0397966101694915"
        }
    ]


@router.post('/foryou')
def recommended_for_you(user=Depends(get_current_user), db: Session = Depends(get_db)):
    # response = personalizeRt.get_recommendations(
    #     recommenderArn='arn:aws:personalize:ap-south-1:296410630894:recommender/foryou',
    #     userId=user.user_id,
    #     numResults=10
    # )
    # data = response['itemList']
    # lis = []
    # for i in range(0, len(data)):
    #     lis.append(data[i]['itemId'])
    # result = crud.get_items_by_item_id(db=db, item_ids=lis)
    # return result
    return [
        {
            "item_id": 456163086,
            "product_name": "Woody(1)",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 93,
            "index_code": "A",
            "section_no": 16,
            "description": "Wide top in sweatshirt fabric with a lined drawstring hood, kangaroo pocket and ribbing at the cuffs and hem.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 308,
            "department_no": 1676,
            "index_group_no": 1,
            "garment_group_no": 1002,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 547780003,
            "product_name": "Basic sweatpants",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 7,
            "index_code": "D",
            "section_no": 51,
            "description": "Trousers in soft sweatshirt fabric with an elasticated drawstring waist, side pockets and ribbed hems. Soft brushed inside.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 272,
            "department_no": 1643,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.022864406779661"
        },
        {
            "item_id": 715624001,
            "product_name": "Becka hoodie",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "D",
            "section_no": 51,
            "description": "Long-sleeved top in soft sweatshirt fabric with a jersey-lined, drawstring hood, kangaroo pocket and ribbing at the cuffs and hem. Soft brushed inside.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 308,
            "department_no": 1643,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 720125001,
            "product_name": "SUPREME RW tights",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports tights in fast-drying functional fabric with a wide waistband to hold in and shape the waist. Regular waist with a concealed key pocket in the waistband.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 273,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 740922001,
            "product_name": "Veronica seamless bra",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Fully lined sports bra in fast-drying functional fabric. Lightly padded cups with removable inserts, adjustable shoulder straps and a racer back. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 254,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 757303014,
            "product_name": "HONEY seamless bra (1)",
            "product_group_name": "Underwear",
            "colour_group_code": 6,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports bra in fast-drying functional fabric with jacquard-patterned details, removable inserts, adjustable shoulder straps that cross at the back and wide ribbing at the hem. Light support. The bra is designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 306,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0304915254237288"
        },
        {
            "item_id": 759871002,
            "product_name": "Tilda tank",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 9,
            "index_code": "D",
            "section_no": 80,
            "description": "Cropped, fitted top in cotton jersey with narrow shoulder straps.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 253,
            "department_no": 3936,
            "index_group_no": 2,
            "garment_group_no": 1002,
            "price": "0.0050677966101694"
        },
        {
            "item_id": 791587015,
            "product_name": "Speedy conscious tee",
            "product_group_name": "Garment Upper body",
            "colour_group_code": 92,
            "index_code": "S",
            "section_no": 5,
            "description": "Straight-cut sports top in fast-drying mesh with short sleeves and a rounded hem. Slightly longer at the back. The polyester content of the top is recycled.",
            "graphical_appearance_no": 1010016,
            "product_type_no": 255,
            "department_no": 8316,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0254067796610169"
        },
        {
            "item_id": 852584001,
            "product_name": "SUPREME RW tights",
            "product_group_name": "Unknown",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "High-waisted, ankle-length sports tights in fast-drying functional fabric. Wide panel to hold in and shape the waist. Concealed key pocket in the waistband.",
            "graphical_appearance_no": 1010016,
            "product_type_no": -1,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0338813559322033"
        },
        {
            "item_id": 918292001,
            "product_name": "STRONG HW seamless tights",
            "product_group_name": "Garment Lower body",
            "colour_group_code": 9,
            "index_code": "S",
            "section_no": 5,
            "description": "Sports tights in fast-drying functional fabric with jacquard-patterned details. High waist with wide, elasticated ribbing. The tights are designed with the minimum number of seams for a more comfortable fit and increased mobility.",
            "graphical_appearance_no": 1010010,
            "product_type_no": 273,
            "department_no": 8310,
            "index_group_no": 26,
            "garment_group_no": 1005,
            "price": "0.0397966101694915"
        }
    ]
