"""Top-level wrapper for `lib.cash_register.CashRegister`.

Some test runners import `cash_register` from the project root; this module
re-exports the class from `lib.cash_register` so both import styles work.
"""
from lib.cash_register import CashRegister

__all__ = ["CashRegister"]
