from __future__ import annotations

import argparse
import json
from pathlib import Path

from .nexus import stamp_event
from .storage.sqlite import connect, init_db, insert_enriched_event


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="akasha-time-nexus")
    sub = parser.add_subparsers(dest="command", required=True)

    stamp = sub.add_parser("stamp", help="Stamp an event with time context")
    stamp.add_argument("--timestamp", required=True, help="UTC timestamp, e.g. 2026-03-29T21:15:00Z")
    stamp.add_argument("--lat", type=float, required=True)
    stamp.add_argument("--lon", type=float, required=True)
    stamp.add_argument("--event-type", default="observation")
    stamp.add_argument("--title", default="")
    stamp.add_argument("--notes", default="")
    stamp.add_argument("--source", default="manual")
    stamp.add_argument("--timezone", default="UTC")
    stamp.add_argument("--db", default="", help="Optional SQLite database path")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "stamp":
        enriched = stamp_event(
            timestamp_utc=args.timestamp,
            latitude=args.lat,
            longitude=args.lon,
            event_type=args.event_type,
            title=args.title,
            notes=args.notes,
            source=args.source,
            metadata={},
            timezone_name=args.timezone,
        )

        print(json.dumps(enriched.to_dict(), indent=2))

        if args.db:
            conn = connect(Path(args.db))
            init_db(conn)
            event_id = insert_enriched_event(conn, enriched)
            print(f"stored_event_id={event_id}")
