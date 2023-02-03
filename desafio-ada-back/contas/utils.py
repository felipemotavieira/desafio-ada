from datetime import datetime, timedelta


def calc_valor_a_receber(reserva):
    if reserva['comissao_personalizada'] == '':
        return float(reserva['total_da_reserva_sem_imposto'])
    return float(reserva['total_da_reserva_sem_imposto']) - float(reserva['comissao_personalizada'])

def calc_venc_a_pagar(reserva):
    datetime_object = datetime.strptime(reserva['data_de_checkout'], '%d-%m-%Y')
    weekday_today = datetime_object.weekday()

    if weekday_today == 0:
        return datetime_object + timedelta(1)

    days_until_tuesday = (weekday_today - 8) * -1
    return datetime_object + timedelta(days_until_tuesday)

def calc_venc_a_receber_airbnb(reserva):
    datetime_object = datetime.strptime(reserva['data_de_checkin'], '%d-%m-%Y')
    return datetime_object + timedelta(5)

def str_to_date(date):
    if type(date) is str:
        return datetime.strptime(date, '%d-%m-%Y')
    return date

def criar_objs_contas(reserva) -> tuple:
    if reserva['portal'].lower() == 'booking.com':
        conta_a_receber = {
            "tipo": "A receber",
            "valor": calc_valor_a_receber(reserva),
            "vencimento": str_to_date(reserva['data_de_checkout']).date(),
            "propriedade": reserva['nome_alojamento'],
            "reserva": reserva['referencia']
        }

        conta_a_pagar = {
            "tipo": "A pagar",
            "valor": float(reserva['extras_sem_imposto']),
            "vencimento": calc_venc_a_pagar(reserva).date(),
            "propriedade": reserva['nome_alojamento'],
            "reserva": reserva['referencia']
        }

        return (conta_a_receber, conta_a_pagar)

    if reserva['portal'].lower() == 'airbnb.com':
        conta_a_receber = {
            "tipo": "A receber",
            "valor": calc_valor_a_receber(reserva),
            "vencimento": calc_venc_a_receber_airbnb(reserva).date(),
            "propriedade": reserva['nome_alojamento'],
            "reserva": reserva['referencia']
        }

        conta_a_pagar = {
            "tipo": "A pagar",
            "valor": float(reserva['extras_sem_imposto']),
            "vencimento": calc_venc_a_pagar(reserva).date(),
            "propriedade": reserva['nome_alojamento'],
            "reserva": reserva['referencia']
        }

        return (conta_a_receber, conta_a_pagar)

def convert_to_data_type(reserva):
    reserva['data'] = str_to_date(reserva['data'])
    reserva['data_de_checkin'] = str_to_date(reserva['data_de_checkin'])
    reserva['data_de_checkout'] = str_to_date(reserva['data_de_checkout'])
    return reserva
