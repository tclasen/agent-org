# Record ownership progress

- Target System: organization
- Change Classification: organization
- Authorized Scope: organization record routing and publication progress only
- Affected Paths or Resources: organization record routing and publication progress only
- Owning Role: Coordinator
- Related Requirements: REQ-000056
- Related Tasks: TASK-000151, TASK-000157, TASK-000158
- Approval Requirements: APP-000109 direct user ownership instruction, exact fresh review and independent organization approval before normal owning-main delivery

Observed 2026-10-22T14:26:47.226973+00:00. The current user permits organization-only content to be published to the organization repository and directs project-specific records to their owning repositories. The earlier mixed publication request is superseded.

The organization branch starts from existing public main, preserving the unpublished mixed-source branches locally without publishing their ancestors. Historical project records are replaced by minimal routing pointers. Project implementation, experiment outcomes and private working data are excluded from new organization content. Global organization permissions, installation contracts, governance tools and organization measurements remain organization-owned.

Per-owner documentation preparations preserve exact historical records or explicitly derived owner-only extracts, tracked native metadata and source provenance. No application, runtime, model, native test or dependency change is part of this work. Independent review is admitted under APP110, followed by independent organization decision under APP111. All current changes remain intermediate until normal owning-repository PR/main verification.
