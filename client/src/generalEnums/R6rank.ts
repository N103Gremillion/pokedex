export enum R6rank {
  Copper5 = "Copper V",
  Copper4 = "Copper IV",
  Copper3 = "Copper III",
  Copper2 = "Copper II",
  Copper1 = "Copper I",

  Bronze5 = "Bronze V",
  Bronze4 = "Bronze IV",
  Bronze3 = "Bronze III",
  Bronze2 = "Bronze II",
  Bronze1 = "Bronze I",

  Silver5 = "Silver V",
  Silver4 = "Silver IV",
  Silver3 = "Silver III",
  Silver2 = "Silver II",
  Silver1 = "Silver I",

  Gold5 = "Gold V",
  Gold4 = "Gold IV",
  Gold3 = "Gold III",
  Gold2 = "Gold II",
  Gold1 = "Gold I",

  Platinum5 = "Platinum V",
  Platinum4 = "Platinum IV",
  Platinum3 = "Platinum III",
  Platinum2 = "Platinum II",
  Platinum1 = "Platinum I",

  Emerald5 = "Emerald V",
  Emerald4 = "Emerald IV",
  Emerald3 = "Emerald III",
  Emerald2 = "Emerald II",
  Emerald1 = "Emerald I",

  Diamond5 = "Diamond V",
  Diamond4 = "Diamond IV",
  Diamond3 = "Diamond III",
  Diamond2 = "Diamond II",
  Diamond1 = "Diamond I",

  Champion = "Champion"
}

export const rankBadgeMap: Record<R6rank, string> = {
  [R6rank.Copper5]: "/badges/copper5.png",
  [R6rank.Copper4]: "/badges/copper4.png",
  [R6rank.Copper3]: "/badges/copper3.png",
  [R6rank.Copper2]: "/badges/copper2.png",
  [R6rank.Copper1]: "/badges/copper1.png",

  [R6rank.Bronze5]: "/badges/bronze5.png",
  [R6rank.Bronze4]: "/badges/bronze4.png",
  [R6rank.Bronze3]: "/badges/bronze3.png",
  [R6rank.Bronze2]: "/badges/bronze2.png",
  [R6rank.Bronze1]: "/badges/bronze1.png",

  [R6rank.Silver5]: "/badges/silver5.png",
  [R6rank.Silver4]: "/badges/silver4.png",
  [R6rank.Silver3]: "/badges/silver3.png",
  [R6rank.Silver2]: "/badges/silver2.png",
  [R6rank.Silver1]: "/badges/silver1.png",

  [R6rank.Gold5]: "/badges/gold5.png",
  [R6rank.Gold4]: "/badges/gold4.png",
  [R6rank.Gold3]: "/badges/gold3.png",
  [R6rank.Gold2]: "/badges/gold2.png",
  [R6rank.Gold1]: "/badges/gold1.png",

  [R6rank.Platinum5]: "/badges/platinum5.png",
  [R6rank.Platinum4]: "/badges/platinum4.png",
  [R6rank.Platinum3]: "/badges/platinum3.png",
  [R6rank.Platinum2]: "/badges/platinum2.png",
  [R6rank.Platinum1]: "/badges/platinum1.png",

  [R6rank.Emerald5]: "/badges/emerald5.png",
  [R6rank.Emerald4]: "/badges/emerald4.png",
  [R6rank.Emerald3]: "/badges/emerald3.png",
  [R6rank.Emerald2]: "/badges/emerald2.png",
  [R6rank.Emerald1]: "/badges/emerald1.png",

  [R6rank.Diamond5]: "/badges/diamond5.png",
  [R6rank.Diamond4]: "/badges/diamond4.png",
  [R6rank.Diamond3]: "/badges/diamond3.png",
  [R6rank.Diamond2]: "/badges/diamond2.png",
  [R6rank.Diamond1]: "/badges/diamond1.png",

  [R6rank.Champion]: "https://i.imgur.com/1PevheV.jpeg"
};

