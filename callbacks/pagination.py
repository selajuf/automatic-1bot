from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards import fabrics
from data.subloader import get_json

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    smiles = await get_json("festivali.json")
    
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"<a href='{smiles[page][0]}'>{smiles[page][1]}</a> (тут встроил ссылку фотки в текст, надеюсь так можно)",
            reply_markup=fabrics.paginator(page)
        )
    await call.answer()