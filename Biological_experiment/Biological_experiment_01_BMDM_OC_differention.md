# Protocol: In Vitro Differentiation of Osteoclasts from Bone Marrow-Derived Monocytes (BMDMs)

## ⚠️ Important Considerations
**Consistency in Growth Factors:** For optimal reproducibility, maintain consistency in your source of Macrophage Colony-Stimulating Factor (M-CSF) throughout the entire protocol. 
* **Path A (Precise Control):** Use Recombinant M-CSF (30–50 ng/mL) for all steps. This is a purified protein and offers precise control.
* **Path B (Cost-Effective):** Use 10% L929 Conditioned Medium (L929-CM) for all steps. L929-CM is a mixture containing M-CSF and other undefined cytokines. 
* *Avoid switching between recombinant M-CSF and L929-CM midway through differentiation*, as this introduces extra signaling stimuli and reduces experimental rigor.

---

## 1. Reagents and Materials

### Media & Buffers
* **Incomplete α-MEM** (Gibco, Cat #: 12561, 500 mL): Contains 1% Penicillin-Streptomycin (P/S). *Note: No FBS, no ribonucleosides/deoxyribonucleosides.*
* **Complete α-MEM**: Incomplete α-MEM supplemented with 10% Fetal Bovine Serum (FBS).
* **PBS (with 1% P/S)**: Kept cold for dissection and washing.
* **Versene / PBS-EDTA**: 0.5 mM EDTA in PBS. *(Preparation: Mix 50 mL PBS with 50 µL of 1000X [0.5 M] EDTA stock).*

### Growth Factors & Cytokines
* **Recombinant Mouse M-CSF** (e.g., R&D Systems, Cat #: 216-MC). Stock concentration: 30 ng/µL.
* **Recombinant Mouse RANKL** (e.g., R&D Systems, Cat #: 462-TEC). Stock concentration: 1.65 µg/µL.
* **L929 Conditioned Medium (L929-CM)**: Used as an M-CSF substitute *(See Appendix for preparation)*. Store at -20°C or -80°C.

---

## 2. Procedure: Bone Marrow Harvest & Monocyte Isolation

### Day 1: Euthanize, Dissect, and Extract
1. **Euthanasia:** Euthanize 6- to 8-week-old mice according to institutional IACUC guidelines.
2. **Dissection:** Dissect the hind limbs to expose the femur and tibia. Strip away all muscle tissue to isolate the bones. Place cleaned bones immediately in a 3 cm dish containing cold PBS (+P/S).
3. **Tube Preparation:** For each mouse, prepare a "nesting tube" system: use a heated needle to drill a small hole in the bottom of a 0.5 mL microcentrifuge tube, and place it inside a 1.5 mL tube.
4. **Extraction:** Cut off the epiphyses (heads) of the femur and tibia. Insert the bones (cut end down) into the 0.5 mL tube. Centrifuge at **3,000–5,000 x g for 15 seconds** to flush the marrow into the 1.5 mL collection tube. Discard the bones and the 0.5 mL tube.
5. **Washing:** Resuspend the bone marrow pellet in 1 mL of cold PBS by gently pipetting up and down. Transfer to a 15 mL conical tube containing 8 mL of cold PBS.
6. **Centrifugation:** Spin at **500 x g for 5 minutes**. Discard the supernatant.
7. **Second Wash:** Resuspend the pellet in 5 mL of incomplete α-MEM, vortex gently, and spin again at **500 x g for 5 minutes**.
8. **Initial Seeding:** Resuspend the pellet in Complete α-MEM. Seed into a 10 cm dish containing **9 mL of Complete α-MEM + 1 mL L929-CM** (or 30 ng/mL recombinant M-CSF). Incubate overnight at 37°C, 5% CO₂.

### Day 2: Depletion of Mesenchymal Stem Cells (MSCs)
1. In the morning, gently swirl the 10 cm dish.
2. Collect the liquid culture medium (supernatant) and transfer it to a 15 mL tube. 
   > **Note:** The attached cells left behind in the dish are primarily MSCs and fibroblasts. Discard this dish.
3. Centrifuge the collected supernatant at **500 x g for 5 minutes** to pellet the non-adherent monocytes.
4. Resuspend the pellet and seed into a fresh 10 cm dish containing **9 mL of Complete α-MEM + 1 mL L929-CM** (or M-CSF).

### Day 3: Observation & Supplementation
1. In the afternoon, observe the cells under the microscope. You should see floating cellular debris and small, round cells beginning to attach to the bottom (these are your monocytes/macrophage precursors).
2. **Supplementation:** If using recombinant M-CSF instead of L929-CM, add M-CSF to reach a final concentration of 50 ng/mL. 
   > **Calculation Note:** For a 10 mL culture volume requiring 50 ng/mL final concentration (500 ng total), add **16.7 µL** of your 30 ng/µL M-CSF stock.

---

## 3. Procedure: Osteoclast (OC) Induction

### Day 4: Detachment and Re-plating
1. **Washing:** Wash cells three times with PBS. Direct the pipette tip against the wall of the dish to avoid flushing away attached cells.
   > *Check Confluency:* If confluency is low, add 9 mL Complete α-MEM + 1 mL L929-CM and allow proliferation for one more day. If high, proceed to detachment.
2. **Detachment:** Add 4 mL of cold Versene (PBS-EDTA) and incubate the plate at 4°C for 6 to 30 minutes. 
3. **Collection:** Detach cells by gentle pipetting (avoid aggressive scraping). Transfer to a tube and spin down. Resuspend in 3 mL of Complete α-MEM supplemented with 10% L929-CM (or 30-50 ng/mL M-CSF).
4. **Counting & Plating:** Count the cells. *(Expected yield: ~0.6 × 10⁶ cells per two hind limbs; ~2.3 × 10⁶ for 4 mice).* 
5. Plate the cells according to your downstream assay needs. 
   > **Recommended Plating Densities:**
   > * **96-well plate:** 30,000 – 40,000 cells/well in 200 µL volume. *(Note: BMDMs require higher seeding densities than RAW 264.7 cells, which only need ~3,000 cells/well. 20K cells/well is often insufficient for downstream transfections requiring 70% confluency).*
   > * **12-well plate:** 3.0 × 10⁵ cells/well.
   > * **6-well plate (for qPCR):** 6.0 × 10⁵ cells/well.

### Day 5 onwards: Differentiation
1. Allow cells to attach and proliferate for 24 hours. Monocytes will initially appear round, then attach and flatten.
2. **Induction Medium:** Change the medium to Complete α-MEM containing **10% L929-CM** (or 30-50 ng/mL M-CSF) **AND 50–100 ng/mL His-RANKL**.
3. **Maintenance:** Change the induction medium every 2–3 days. Monitor cell morphology carefully.
4. **Observation & Staining:** Check daily for the formation of multinucleated Osteoclasts (OCs). OCs typically begin appearing 3–5 days after the initial addition of RANKL.
   > **Critical:** Proceed to TRAP staining or lyse cells immediately upon observing mature OC formation, as they are fragile and may undergo apoptosis/disintegrate within 24 hours of maturation.

---

## Appendix: Preparation of L929 Conditioned Medium (L929-CM)

L929-CM is a cost-effective substitute for recombinant M-CSF. It is stable for ~1 year at −20°C.

### A. Cell Maintenance & Passage
1. **Culture Conditions:** Maintain L929 cells in DMEM supplemented with 10% heat-inactivated FBS (56°C for 30 min) and 1% P/S + L-glutamine. Cultivate at 37°C, 5% CO₂ in T-75 flasks or 10 cm dishes.
2. **Passaging (Weekly):**
   * Wash the cell monolayer with 10 mL warm DPBS.
   * Add 1.0 mL Trypsin-EDTA; incubate at 37°C for ≤ 5 minutes.
   * Neutralize with 10 mL complete medium and pipette to break up clumps.
   * Split at approximately 1:20 (e.g., 1 drop of suspension into a new T-75 flask with 20 mL medium).

### B. Conditioned Medium Production
1. **Seeding:** Prepare eight T-150 triple flasks. Add 150 mL complete medium to each. Seed **2.5 × 10⁵ cells per 150 cm²** surface.
2. **Week 1 Incubation:** Incubate for 7 days. Several times during the week, carefully tip each flask upright and lay it flat again to ensure even cell distribution.
3. **Week 1 Collection:** On Day 7, collect the medium. Filter through a **0.2 µm filter**. Aliquot into 50 mL tubes and store at −20°C. *(This is Week 1 L929-CM).*
4. **Week 2 Incubation:** Add 150 mL of *fresh, pre-warmed* culture medium back into the same flasks containing the cells. Incubate for another 7 days.
5. **Week 2 Collection:** On Day 14, collect the medium, discard the flasks/cells, and filter through a 0.2 µm filter. *(Note: This step may require multiple filters due to high cellular debris). Aliquot and store at −20°C. *(This is Week 2 L929-CM).*

### C. Mixing and Usage
* **Potency:** Week 2 L929-CM is typically more potent due to higher concentrations of accumulated cytokines.
* **Final Preparation:** Before using for bone marrow cultures, thaw and mix equal volumes of Week 1 and Week 2 L929-CM (1:1 ratio).
* **Usage:** Use at a **1:10 dilution (10% final concentration)** in your Complete α-MEM to replace recombinant M-CSF. Ensure you test a new batch of L929-CM using a bioassay for BMDM growth before applying it to critical experiments.
