## Практика Stock Portfolio
  
Написать упражнение Stock Portfolio по TDD, используя все знания о тестах и тестируемом коде.


**User Story:** 
Клиент биржевого брокера хочет видеть свой портфель акций, чтобы запланировать финансовую стратегию и следующие операции.
 
**Задача:** Предоставить приложение, способное записывать операции покупки и продажи клиента и отображать информацию в соответствии со сценарием ниже. Для простоты – одновременно оно должен работать только для одного пользователя. Помните, что цена акций постоянно меняется, поэтому она не должна быть захардкожена, а должна передаваться в тесте.
  
**Поддерживаемый сценарий:**
```
Given I bought 1000 shares of "Old School Waterfall Software LTD" on 14/02/1990
 And I bought 400 shares of "Crafter Masters Limited" on 09/06/2016
 And I bought 700 shares of "XP Practitioners Incorporated" on 10/12/2018
 And I sold 500 shares of "Old School Waterfall Software LTD" on 11/12/2018
 And the current share value of "Old School Waterfall Software LTD" is $5.75
 And the current share value of "Crafter Masters Limited" is $17.25
 And the current share value of "XP Practitioners Incorporated" is $25.55
 When I print my current portfolio
 Then the outcome displayed should be:

company | shares | current price | current value | last operation
Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018
Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016
XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018
```

[Оригинальное упражнение](https://github.com/AgileTechPraxis/outside-in-kata)

**Ответ:**
  
[Код и тесты](/practice/day2/05_stock_portfolio/)
