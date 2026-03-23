This module customizes the display order of discount totals in
Sale Order reports.

By default, some modules display the totals in the following order:

- Total
- Discount
- Total Without Discount

This module reorganizes the totals section in printed Sale Order reports so that the order becomes:

- Total Without Discount
- Discount
- Total

The implementation is done entirely through QWeb report inheritance,
without modifying any business logic, tax computation, or sales behavior.

It also disables the legacy discount rows added by other modules
to prevent duplicated lines in the report output.
