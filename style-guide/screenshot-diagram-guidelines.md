# Screenshot and diagram guidelines

At Rackspace, we strive to deliver ***Fanatical Support***® through exceptional
documentation. Images are an essential part of helpful, clear, and concise content. Follow the standards in this section when creating images for your documents.

- [Screenshot guidelines](#screenshot-guidelines)
- [Diagram guidelines](#diagram-guidelines)
- [Next steps](#next-steps)

**Note:** These guidelines conform to all of the rules outlined in the [writing style guide](https://github.com/rackerlabs/docs-rackspace/blob/master/style-guide/basic-writing-guidelines.md).

## Screenshot guidelines and process

When your content references a user interface (UI), consider whether you need to include screenshots. Screenshots can be helpful when text alone cannot adequately convey instructions, and users like screenshots and find them useful. However, screenshots are difficult and time-consuming to maintain and present translation problems. Therefore, the use of screenshots within your article should be kept to a minimum.

- [Screenshot alternatives](#screenshot-alternatives)
- [When to use screenshots](#when-to-use-screenshots)
- [When not to use screenshots](#when-not-to-use-screenshots)
- [Before you create a screenshot](#before-you-create-a-screenshot)
- [Screenshot checklist](#screenshot-checklist)

### Screenshot alternatives

As an alternative to screenshots, use the correct names of the UI labels with which the user must interact and the values that they must choose or enter. Show the names of buttons, options, check boxes, menus, windows, dialog boxes, and so on as they appear on the UI. For example, for straightforward instructions like, "To open a file, select **File > Open**," a screenshot is not required.

### When to use screenshots

- Orient users in a complicated or long procedure

- Show complex windows or dialog boxes, such as those that contain multiple subsets of information, with free-form text fields and many options available for selection.

### When not to use screenshots

- Code samples (instead, show code samples in code blocks)

- Dialog boxes that are easy to understand, such as drop-down lists and option buttons with few or no free-form text fields

- Confirmation boxes

- License agreement boxes

- Message text (instead show message text within regular text)

- Progress bars

- Welcome windows

- Wizard pages, especially Welcome pages and other simple pages

- Tables created in another authoring tool

### Before you create a screenshot

Install Jing to capture and edit screenshots. Jing is available as a free download at https://www.techsmith.com/jing.html.

To learn how to take a screenshot and make a callout in Jing, use the tutorial [capture an image](https://www.techsmith.com/tutorial-jing-capture-an-image.html)

**Note:** Jing does not support Linux distributions, but you can use other programs such as gscreendemp, greenshot, and shutter on Linux.

### Screenshot checklist

Use the following checklist to keep your screenshots up to standard:

- [ ] **Size**: Must not be larger than 600 pixels wide.
- [ ] **Callouts**: Use only arrows and boxes for callouts. To learn how to add a callout using Jing.
- [ ] **Callout color**: Use **Red**(hexadecimal color **FF0000**) for all callouts.
- [ ] **File name**: Must be unique and meaningful, enabling easy differentiation between screenshots.

To learn how to take a screenshot and make a callout in Jing, use the tutorial [capture an image](https://www.techsmith.com/tutorial-jing-capture-an-image.html)

## Diagram guidelines

Diagrams can be useful tools to help users visualize complex processes in a simplified fashion. However, diagrams can sometimes be too simplistic, confusing the user instead of providing help. Although the decision about whether a diagram might be helpful depends on the context of each document and the discretion of each writer.

- [When to use diagrams](#when-to-use-diagrams)
- [When not to use diagrams](#when-not-to-use-diagrams)
- [Before you create a diagram](#before-you-create-diagram)
- [Diagram checklist](#diagram-checklist)

### When to use diagrams

- When there is evidence of a process, whether the process is automated or manual. As a general rule, a process can be defined as the exchange of data between two points. Points can be anything from a API endpoint to a user entering commands through the Cloud Control Panel.

- When clarifying configurations and settings, such as the architecture for virtual servers.

- When defining a complex workflow within a Rackspace product.

### When not to use diagrams

- When a workflow is too simplistic, such as creating a cloud server using the control panel.
- When there is no interaction with a Rackspace product.

### Before you create a diagram

#### Software

Use [draw.io](https://www.draw.io/) to create your diagrams. Draw.io enables you to create diagrams directly in your web browser of choice.

Draw.io provides instructions on how to use the tool in the [Draw.io Online User Manual](https://support.draw.io/display/DO/Draw.io+Online+User+Manual). These instructions are a good start for getting familiar with using Draw.io.

#### Icons, stencils, and shapes

You also need to download Rackspace's library of product icons and stencils. These icons, stencils, and shapes are considered **objects**.

The product icons are blue and located in [this zip file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/ProductIcons.zip).

Stencils are used to represent certain functions and hardware such as the world wide web or a server. These stencils are black and located in [this zip file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/RackspaceDiagramIcons.zip).

**Note:** A library of Rackspace icons and their meanings can be found in [this PDF file](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/rackspace-icon-library[1].pdf).

With your icons downloaded, you can being making diagrams in Draw.io.

### How to use Draw.io

Draw.io provides instructions on how to use the tool in the [Draw.io Online User Manual](https://support.draw.io/display/DO/Draw.io+Online+User+Manual). These instructions are a good start for getting familiar with using Draw.io.

### Diagram checklist

Use the following checklists when creating diagrams:

#### Properties

Each diagram property can be found on the right of the Draw.io main screen under **Diagrams**.

- [ ] **Paper size**: Must be set to **A4 (210 mm x 297 mm)** and **Landscape**.

- [ ] **Background color**: Must be set to **none**.

- [ ] **File format**: All diagrams must be saved as an editable SVG file.

   1. Click **File > Save As**.
   2. Type a descriptive name for the file, and replace `.xml` with `.svg` at the end of the file name. The file will save to your local directory.

- [ ] **File name**: Must be unique and meaningful, enabling easy differentiation between diagrams.

#### Text formatting

- [ ] **Font**: Must be set to **Helvetica**.

- [ ] **Titles:** Must be **bolded**, aligned **left**, and be at least **24px** in size.

#### Objects

- [ ] **Product icons**: Represents it's corresponding product. Product icons are always blue.

   ![Cloud Images stencil](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/images.png)

   **Note:** If you find a Rackspace product icon that is not blue, email how-to@rackspace.com and a member of our team will create a blue version of the icon.

- [ ] **Stencils**: Each stencil used represents a concept or function equal or similar to it's definition in the [Rackspace library of icons](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/zip/rackspace-icon-library[1].pdf). Stencils that are **not** Rackspace products should always appear in black.

- [ ] **Labels**: All product icons, stencils, and shapes, must be labeled according to their function within the diagram.

#### Lines and arrows

- [ ] **Line usage**: Lines are used to connect and display a relationship between two or more objects.

- [ ] **Line width**: Must be at least **2pt**. You can change the width of a line in the **Format Panel** under **Style** when you select the line.

- [ ] **Line shape**: Keep lines straight unless a line needs to change direction.

- [ ] **Rounded line corners**: If a line changes direction, the corner in which the change of direction occurs must be rounded. You can change to rounded corners by selecting the line, going to the **Format PAnel** under **Style**, and selecting **Rounded** in the dropdown menu.

- [ ] **Solid lines**: Show a direct relationship between objects.

   ![Example of solid lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/solid-lines.png)

- [ ] **Dashed lines**: Group objects that are connected through a network.

   ![Example of dashed lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/dashed-lines.png)

- [ ] **Dotted lines**: Show the traveling of data inputted by a user.

   ![Example of dotted lines](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/dotted-lines.png)

- [ ] **One-way and two-way arrows:** Represent direct interactions between two or more stencils. If a stencil is attached to an arrow, it implies that the product represented by the stencil needs to interact with another piece of the diagram.

   In the following example, the CDN management service needs to interact with the CDN to perform it's function. Similarly, the CDN needs to be managed by the CDN management service. The relationship is two-way, so the line has arrows on both ends pointed to both stencils.

   ![Example of one-way and two-way arrows](https://github.com/rackerlabs/docs-rackspace/blob/master/_assets/img/arrowsscreenshot.png)

## Next steps

- [Contribute to our Rackspace How-To support network](https://github.com/rackerlabs/rackspace-how-to)

- [Contribute to our Rackspace core infrastructure user guide](https://github.com/rackerlabs/docs-core-infra-user-guide)
