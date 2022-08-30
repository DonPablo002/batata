# Bot token.
BOT_TOKEN = "5645889158:AAFKW8l_LXhpSM24ILZwgbgep4RfTtSc0x8"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 10581891
API_HASH = "b73705b4284f02e6f80f39d00d46fef2"

# CHAT DE ERROS
LOG_CHAT = -1001520108802

# LOGS DE COMPRAS E ADD SALDO
ADMIN_CHAT = -1001520108802

# CHAT DE COMPRAS PARA CLIENTE
CLIENT_CHAT = -1001520108802
# Quantas atualiza��es podem ser tratadas em paralelo.
# N�o use valores altos para servidores low-end.
WORKERS = 20

# Os administradores podem acessar o painel e adicionar novos materiais ao bot.
ADMINS = [5193376857, 1853137977]

# Sudoers t�m acesso total ao servidor e podem executar comandos.
SUDOERS = [5193376857]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []
