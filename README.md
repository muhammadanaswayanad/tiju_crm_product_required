# TIJU CRM Product Required (Enhanced: Course Required by Stage)

## Module Information

-   **Module Name:** TIJU CRM Product Required (now CRM Course Required by Stage)
-   **Technical Name:** `tiju_crm_product_required`
-   **Author:** Tiju
-   **Version:** 16.0.1.0.0 (Manifest shows 1.0, consider aligning)
-   **License:** LGPL-3
-   **Category:** Sales/CRM

## Summary

This Odoo module enhances the standard CRM functionality. Initially designed to make the 'Product' field globally mandatory on the Opportunity form, it has been updated to conditionally require a 'Course' (a specific type of product) based on the CRM stage of an opportunity.

## Purpose

The primary goal of this module is to enforce data integrity within the CRM module by:
1.  Allowing administrators to define specific CRM stages where selecting a 'Course' is mandatory.
2.  Ensuring that users select a 'Course' for an opportunity when it is in or moves to such a configured stage.

## Key Features

-   Adds a boolean field `course_required` to the `crm.stage` model.
-   Allows administrators to mark specific CRM stages as requiring a 'Course'.
-   Adds a `course_id` (Many2one to `product.product`, filtered for services) field to the `crm.lead` model.
-   Makes the `course_id` field dynamically required on the Opportunity form based on the `course_required` setting of the current stage.
-   Includes a validation (`@api.constrains`) to prevent saving an opportunity in a stage that requires a course if the course is not set.

## Dependencies

-   **CRM (`crm`)**: Base Odoo CRM module.
-   **Product (`product`)**: Base Odoo Product module (for `product.product` model).

## Configuration

1.  Navigate to **CRM > Configuration > Stages**.
2.  Select or create a CRM stage.
3.  In the stage form, you will find a new checkbox: **"Course Mandatory in this Stage?"**.
4.  Check this box if opportunities in this stage must have a 'Course' selected.
5.  Save the stage configuration.

## Installation

1.  Download or clone this module.
2.  Place the `tiju_crm_product_required` folder into your Odoo addons path.
3.  Restart the Odoo server.
4.  Go to **Apps** in your Odoo instance.
5.  Click on **Update Apps List**.
6.  Search for "CRM Course Required by Stage" (or "TIJU CRM Product Required") and click **Install**.

## Usage

Once installed and configured:

1.  Navigate to the **CRM** module.
2.  Create a new Opportunity or edit an existing one.
3.  When an Opportunity is in a stage that has "Course Mandatory in this Stage?" checked:
    *   The 'Course' field on the Opportunity form will become visually mandatory.
    *   The system will prevent saving the Opportunity or moving it to this stage if the 'Course' field is empty, raising a validation error.
4.  If the stage does not require a course, the 'Course' field will behave as a normal optional field.

## Technical Details

-   **Models Modified:**
    -   `crm.stage`: Added `course_required` (Boolean) field.
    -   `crm.lead`: Added `course_id` (Many2one `product.product`) field.
        -   `_onchange_stage_id_for_course_required`: Method to update UI context for `course_id` field's `required` attribute.
        -   `_check_course_required`: Constraint to validate `course_id` based on `stage_id.course_required`.
-   **Views Modified:**
    -   `crm.stage.form` (via `crm_stage_form_view_inherit`): Added `course_required` field to the stage form.
    -   `crm.lead.view.form` (via `crm_lead_view_form_inherit_product_required`): Added `course_id` field to the opportunity form, with conditional `required` attribute based on context.

## Credits

-   **Developer:** Tiju
