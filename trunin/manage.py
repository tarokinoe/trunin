#!/usr/bin/env python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="", choices=[
        'start', 'send_photo', 'dbcreate'
    ])
    args = parser.parse_args()
    if args.command == 'start':
        from bot import updater
        updater.start_polling()

    if args.command == 'send_photo':
        from tgm import send_photo
        send_photo()

    if args.command == 'dbcreate':
        import models
        models.Base.metadata.create_all(models.engine)
