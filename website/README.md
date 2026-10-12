<p align="center">
  <a href="#english">🇬🇧 English</a>
  &nbsp;·&nbsp;
  <a href="#russian">🇷🇺 Русский</a>
</p>

<a id="english"></a>

# Fast Scheduler for Telegram

Fast Scheduler is a Telegram bot for preparing, scheduling, and managing posts in Telegram channels.

<p align="center">
  <a href="https://t.me/FastSchedulerBot"><strong>▶ Try @FastSchedulerBot</strong></a>
</p>

## What makes it different

### Schedule many messages from one message

You can send several date/message pairs in one conversation instead of creating every scheduled post separately. Each message is separated by an empty line:

```text
2026-12-24 18:00
First holiday message

2026-12-25 12:00
Second holiday message

2026-12-31 23:00
New Year message
```

The bot reads each date/time together with the content that follows it and creates the scheduled messages at once. The exact accepted date and time formats are shown by the bot during the scheduling flow. Each message keeps its own text and media settings.

### Formatting is preserved

Scheduled text keeps supported Telegram rich formatting and message entities, including bold, italic, links, code, spoilers, custom emoji and other formatting from the original message. The bot validates unsupported inline-button syntax before saving a post.

## Main features

- Schedule one-time channel messages for a chosen date and time.
- Create several scheduled messages in one batch using date/message pairs.
- Use a user or channel timezone instead of relying on the server timezone.
- Create recurring messages using simple schedules or custom five-field cron expressions.
- View upcoming scheduled and recurring messages in lists and the calendar.
- Search scheduled content and open its actions.
- Edit, delete, duplicate, replace, preview, or otherwise manage supported scheduled messages.
- Send text, photos, videos, documents, animations, audio, voice messages, video notes, polls, locations and other Telegram-supported content where the current Telegram API and bot permissions allow it.
- Keep captions and supported formatting together with media.
- Add clickable inline buttons with configurable styles.
- Add a reusable signature automatically at the beginning or end of posts.
- Connect one or more Telegram channels according to the current account limits.
- Post through the main bot or connect a separate sender bot so channel posts appear from that bot.
- Use Media Storage to save reusable Telegram media references and select them later without uploading the same file again.
- Choose a media mode for a batch: reuse one item, assign media sequentially, assign it randomly, or select items from Media Storage.
- Export and back up account data, then import supported backups when needed.
- View sending statistics, channel analytics, leaderboards and automated reports.
- Use language selection (English, Español, Русский), help articles, feedback, referral program and support flows.
- Manage Premium through Telegram Stars when Premium purchases are enabled.

Available limits and actions depend on the current plan, Telegram permissions, Telegram API restrictions, and the message type.

## Media modes

When a scheduled batch contains several messages, the bot can handle media in different ways:

1. **One media item** — reuse the selected media with the scheduled messages.
2. **Sequential media** — the first media item is assigned to the first message, the second to the second, and so on.
3. **Random media** — the bot chooses from the provided media for each message.
4. **Media Storage** — select previously saved Telegram media instead of uploading it again.

Limits and available media types depend on the account plan, Telegram restrictions, and the connected channel's permissions.

## A typical setup

1. Open [@FastSchedulerBot](https://t.me/FastSchedulerBot).
2. Complete the built-in tutorial.
3. Add the bot as a channel administrator with at least **Post Messages** permission.
4. Connect the channel in the bot.
5. Optionally connect a sender bot and add it as an administrator in the same channel.
6. Set your timezone.
7. Choose **Schedule**, send the content, choose the date/time or batch format, select the channel and media options, then confirm.
8. Manage the result from **Messages**, **Calendar**, or **Search**.

For editing or deleting channel posts, the bot or sender bot may also need the corresponding Telegram administrator permissions.

## Recurring messages

Recurring messages can be configured with built-in options or a custom cron expression. Examples:

```text
0 9 * * 1     every Monday at 09:00
30 18 * * *   every day at 18:30
0 8 1 * *     on the first day of every month at 08:00
```

Recurring messages keep their selected content, media, channel, and schedule until you edit, pause, or delete them.

## Premium

Premium availability and limits are shown inside the bot. The current user-facing payment flow uses **Telegram Stars**. The available plan terms are displayed before payment; recurring and prepaid/one-time terms are not interchangeable, so review the plan description in Telegram before confirming.

## Legal documents

- [Privacy Policy](legal/privacy.html)
- [Terms of Service](legal/terms.html)
- [Refund Policy](legal/refundpolicy.html)

This README describes the implemented product at a high level. Telegram's own rules, channel permissions, plan limits, and the bot's current in-app instructions control when a particular action is available.

<p align="right"><a href="#russian">🇷🇺 Читать по-русски ↓</a></p>

---

<a id="russian"></a>

# Fast Scheduler для Telegram

Fast Scheduler — это Telegram-бот для подготовки, планирования и управления публикациями в Telegram-каналах.

<p align="center">
  <a href="https://t.me/FastSchedulerBot"><strong>▶ Попробовать @FastSchedulerBot</strong></a>
</p>

## Главное отличие

### Несколько публикаций одним сообщением

Не нужно создавать каждую запланированную публикацию отдельно. Можно отправить несколько пар «дата/время + текст» в одном сообщении — каждая публикация отделяется пустой строкой:

```text
2026-12-24 18:00
Первое праздничное сообщение

2026-12-25 12:00
Второе праздничное сообщение

2026-12-31 23:00
Новогоднее сообщение
```

Бот связывает каждую дату и время со следующим содержимым и создаёт все запланированные публикации сразу. Поддерживаемые форматы даты и времени бот показывает во время планирования. У каждой публикации сохраняются собственный текст и настройки медиа.

### Сохранение форматирования

Запланированный текст сохраняет поддерживаемое Telegram форматирование: жирный и курсивный текст, ссылки, код, спойлеры, custom emoji и другие возможности исходного сообщения. Перед сохранением бот проверяет неподдерживаемый синтаксис inline-кнопок.

## Основные функции

- Планирование разовых публикаций в канал на выбранную дату и время.
- Создание нескольких публикаций одним сообщением в формате «дата/время + сообщение».
- Использование часового пояса пользователя или канала.
- Повторяющиеся публикации по готовым вариантам или через пятикомпонентное cron-выражение.
- Просмотр запланированных и повторяющихся сообщений в списках и календаре.
- Поиск по запланированному содержимому.
- Просмотр, редактирование, удаление, дублирование, замена и другие доступные действия над сообщениями.
- Поддержка текста, фотографий, видео, документов, анимаций, аудио, голосовых сообщений, видеосообщений, опросов, геопозиций и других типов, разрешённых текущим Telegram API и правами бота.
- Сохранение подписей и поддерживаемого форматирования вместе с медиа.
- Кликабельные inline-кнопки с настраиваемыми стилями.
- Автоматическая подпись в начале или конце публикации.
- Подключение Telegram-каналов в пределах текущих лимитов аккаунта.
- Публикация через основной бот или через отдельный sender bot.
- Media Storage для повторного выбора ранее сохранённых Telegram media без повторной загрузки.
- Режимы медиа для пакетных публикаций: одно медиа, последовательный выбор, случайный выбор или выбор из хранилища.
- Экспорт и резервное копирование данных с возможностью импорта поддерживаемых backup-файлов.
- Статистика отправок, аналитика каналов, рейтинги публикаций и автоматические отчёты.
- Выбор языка (English, Español, Русский), статьи помощи, обратная связь, реферальная программа и поддержка.
- Premium через Telegram Stars, если покупки Premium включены.

Доступные лимиты и действия зависят от текущего тарифа, прав Telegram, ограничений Telegram API и типа сообщения.

## Режимы медиа

Для нескольких запланированных сообщений можно выбрать:

1. **Одно медиа** — использовать выбранный файл для публикаций.
2. **По порядку** — первое медиа к первому сообщению, второе ко второму и так далее.
3. **Случайный выбор** — выбирать медиа из набора для каждой публикации.
4. **Media Storage** — выбрать ранее сохранённые Telegram media.

Ограничения и типы медиа зависят от тарифа, ограничений Telegram и прав в канале.

## Быстрая настройка

1. Откройте [@FastSchedulerBot](https://t.me/FastSchedulerBot).
2. Пройдите встроенный tutorial.
3. Добавьте бота администратором канала минимум с правом **Post Messages**.
4. Подключите канал в боте.
5. При необходимости подключите sender bot и добавьте его администратором в тот же канал.
6. Укажите часовой пояс.
7. Нажмите **Schedule**, отправьте содержимое, выберите дату/время или пакетный формат, канал и параметры медиа, затем подтвердите.
8. Управляйте публикациями через **Messages**, **Calendar** или **Search**.

Для редактирования или удаления публикаций могут понадобиться соответствующие права администратора Telegram.

## Повторяющиеся публикации

Можно выбрать готовый вариант повторения или указать cron-выражение. Примеры:

```text
0 9 * * 1     каждый понедельник в 09:00
30 18 * * *   каждый день в 18:30
0 8 1 * *     первого числа каждого месяца в 08:00
```

Повторяющаяся публикация сохраняет содержимое, медиа, канал и расписание, пока вы не измените, не приостановите или не удалите её.

## Premium

Доступность Premium и лимиты показываются внутри бота. Текущий способ оплаты — **Telegram Stars**. Перед оплатой бот показывает условия конкретного тарифа; условия подписки и разовой покупки различаются, поэтому проверяйте описание тарифа в Telegram перед подтверждением.

## Юридические документы

- [Политика конфиденциальности](legal/privacy.html)
- [Условия использования](legal/terms.html)
- [Политика возвратов](legal/refundpolicy.html)

README описывает функции на высоком уровне. Для конкретного действия действуют правила Telegram, права канала, текущие лимиты тарифа и инструкции, показанные ботом.

<p align="right"><a href="#english">🇬🇧 Back to English ↑</a></p>
