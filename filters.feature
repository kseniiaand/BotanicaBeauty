Feature: Filter functionality
  Scenario Outline: Categories option functionality
    Given The user is on Botanical Beauty shop page
    When The user clicks on Filters on the left side of the page
    And clicks on Categories dropdown
    And chooses <request>
    Then the <result> will appear

 Examples:
    |request                   |result                                                    |
    |Black Friday Deals        | Message 'Sorry, there are no products in this collection'|
    |Christmas Collection      | Message 'Sorry, there are no products in this collection'|
    |Curly Perfection Bundle   | 4 products                                               |
    |Kinky / Coily Love Bundle | 6 products                                               |
    |NEW!                      | 4 products                                               |
    |Treatment Bundle          | 2 products                                               |


  Scenario: Vendors option functionality
    Given The user is on Botanical Beauty shop page
    When The user clicks on Filters on the left side of the page
    And clicks on Vendors  dropdown
    And chooses BotanicaBeauty
    Then all the products will appear

  Scenario: Types option functionality
    Given The user is on Botanical Beauty shop page
    When The user clicks on Filters on the left side of the page
    And clicks on Types dropdown
    And clicks on GiftCards option
    Then all the Gift Cards will appear

  Scenario:Price Range functionality
    Given The user is on Botanical Beauty shop page
    When The user clicks on Filters on the left side of the page
    And moves the Price Range slider to the center where the price is $20
    Then only those products below $20 will appear

  Scenario: Dropdown functionality
    Given The user is on Filters section
    When the user clicks on plus sign next to Categories option
    And all the available filters appear
    And the user click on minus sign
    Then all the available filters disappear



