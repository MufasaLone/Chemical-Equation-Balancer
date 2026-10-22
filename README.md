# Chemical Equation Balancer
Computational chemical equation balancer built entirely with Python's standard library, with no external dependencies.

## What It Does
Enter a chemical equation, click **Confirm**, then the app will show you the balanced chemical equation.

#### Examples of Input and Output:
- Standard Chemical Equation
  
  **Input:** <code>K2Cr2O7 + HCl -> KCl + CrCl3 + H2O + Cl2</code>
  
  **Output:** <code>K2Cr2O7 + 14HCl -> 2KCl + 2CrCl3 + 7H2O + 3Cl2</code>

- Chemical Equation with Hydrates
  
  **Input:** <code>CuSO4·5H2O + NH3 -> [Cu(NH3)4]SO4·H2O + H2O</code>
  
  **Output:** <code>CuSO4·5H2O + 4NH3 -> [Cu(NH3)4]SO4·H2O + 4H2O</code>

- Chemical Equation with Ions

  **Input:** <code>PO4^3- + Ca^2+ -> Ca3(PO4)2</code>
  
  **Output:** <code>2PO4^3- + 3Ca^2+ -> Ca3(PO4)2</code>

- Invalid Chemical Equation

  **Input:** <code>H2 -> H2O</code>
  
  **Output:** <code>Error: Cannot be balanced.</code>

#### Supporting Data:
<table align="center">
  <tr>
    <th>Standard Chemical Equation</th>
    <th>Chemical Equation with Hydrates</th>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/1a364ada-d469-495b-853f-79d9b83d7993" width="100%" alt="Standard Equation">
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/af0418f3-aaa4-4c51-b717-4289ab9ad4da" width="100%" alt="Hydrates">
    </td>
  </tr>
  <tr>
    <th>Chemical Equation with Ions</th>
    <th>Invalid Chemical Equation</th>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/3e56e8ff-7d2b-4689-b07c-d3b57e5ca912" width="100%" alt="Ions">
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/611e8e4d-f27d-4229-b709-255d110cdb89" width="100%" alt="Invalid Equation">
    </td>
  </tr>
</table>

## How to Use
1. Go to [Releases](https://github.com/MufasaLone/Chemical-Equation-Balancer/releases).
3. Download the latest ".exe" file.
4. Install and run.

## Supported Syntax
<table>
  <tr>
    <th colspan="2">Chemical Formula</th>
  </tr>
  <tr>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>Simple Formula</td>
    <td><code>H2O</code></td>
  </tr>
  <tr>
    <td>Parentheses, Brackets, and Braces</td>
    <td><code>K4[Fe(CN)6]</code></td>
  </tr>
  <tr>
    <td>Hydrates ( · )</td>
    <td><code>CuSO4·5H2O</code></td>
  </tr>
  <tr>
    <td>Decimal Subscripts</td>
    <td><code>Fe1.1Te</code></td>
  </tr>
  <tr>
    <td>Ionic Charges ( ^ )</td>
    <td><code>Mg^2+</code></td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="2">Chemical Equation</th>
  </tr>
  <tr>
    <th>Syntax</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><code>-&gt;</code></td>
    <td>Separates reactants from products</td>
  </tr>
  <tr>
    <td><code>+</code></td>
    <td>Separates individual compounds</td>
  </tr>
</table>

*Note: Include spaces around + and -> to ensure compounds are separated correctly.*

## How It Works
Add later...
