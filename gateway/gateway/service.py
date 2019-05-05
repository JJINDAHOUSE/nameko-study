import json

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from gateway.ependencies import Config
from gateway.entrypoints import http
from gateway.exceptions import OrderNotFound, ProductNotFound
from gateway.schemas import CreateOrderSchema, GetOrderSchema, ProductSchema
