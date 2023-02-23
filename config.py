from aiogram import *
import datetime
from Database import *
import aioschedule
from datetime import date
from aiogram.dispatcher.filters import Text
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.message import ContentType
from email_validate import validate, validate_or_fail
import os
import asyncio