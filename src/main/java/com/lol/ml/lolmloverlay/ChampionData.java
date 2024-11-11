package com.lol.ml.lolmloverlay;
import java.util.List;
import java.util.Map;

public class ChampionData {

    private String type;
    private String format;
    private String version;
    private Map<String, Champion> data;

    // Getters and Setters
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public Map<String, Champion> getData() {
        return data;
    }

    public void setData(Map<String, Champion> data) {
        this.data = data;
    }

    public static class Champion {
        private String id;
        private String key;
        private String name;
        private String title;
        private Image image;
        private List<Skin> skins;
        private String lore;
        private String blurb;
        private List<String> allytips;
        private List<String> enemytips;
        private List<String> tags;
        private String partype;
        private Info info;
        private Stats stats;
        private List<Spell> spells;
        private Passive passive;
        private List<Object> recommended;

        // Getters and Setters
        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getKey() {
            return key;
        }

        public void setKey(String key) {
            this.key = key;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }
        public Image getImage() {
            return image;
        }

        public void setImage(Image image) {
            this.image = image;
        }

        public List<Skin> getSkins() {
            return skins;
        }

        public void setSkins(List<Skin> skins) {
            this.skins = skins;
        }

        public String getLore() {
            return lore;
        }

        public void setLore(String lore) {
            this.lore = lore;
        }

        public String getBlurb() {
            return blurb;
        }

        public void setBlurb(String blurb) {
            this.blurb = blurb;
        }

        public List<String> getAllytips() {
            return allytips;
        }

        public void setAllytips(List<String> allytips) {
            this.allytips = allytips;
        }

        public List<String> getEnemytips() {
            return enemytips;
        }

        public void setEnemytips(List<String> enemytips) {
            this.enemytips = enemytips;
        }

        public List<String> getTags() {
            return tags;
        }

        public void setTags(List<String> tags) {
            this.tags = tags;
        }

        public String getPartype() {
            return partype;
        }

        public void setPartype(String partype) {
            this.partype = partype;
        }

        public Info getInfo() {
            return info;
        }

        public void setInfo(Info info) {
            this.info = info;
        }

        public Stats getStats() {
            return stats;
        }

        public void setStats(Stats stats) {
            this.stats = stats;
        }

        public List<Spell> getSpells() {
            return spells;
        }

        public void setSpells(List<Spell> spells) {
            this.spells = spells;
        }

        public Passive getPassive() {
            return passive;
        }

        public void setPassive(Passive passive) {
            this.passive = passive;
        }

        public List<Object> getRecommended() {
            return recommended;
        }

        public void setRecommended(List<Object> recommended) {
            this.recommended = recommended;
        }
    }

    public static class Image {
        private String full;
        private String sprite;
        private String group;
        private int x;
        private int y;
        private int w;
        private int h;

        // Getters and Setters
        public String getFull() {
            return full;
        }

        public void setFull(String full) {
            this.full = full;
        }

        public String getSprite() {
            return sprite;
        }

        public void setSprite(String sprite) {
            this.sprite = sprite;
        }

        public String getGroup() {
            return group;
        }

        public void setGroup(String group) {
            this.group = group;
        }

        public int getX() {
            return x;
        }

        public void setX(int x) {
            this.x = x;
        }

        public int getY() {
            return y;
        }

        public void setY(int y) {
            this.y = y;
        }

        public int getW() {
            return w;
        }

        public void setW(int w) {
            this.w = w;
        }

        public int getH() {
            return h;
        }

        public void setH(int h) {
            this.h = h;
        }
    }

    public static class Skin {
        private String id;
        private int num;
        private String name;
        private boolean chromas;

        // Getters and Setters
        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public int getNum() {
            return num;
        }

        public void setNum(int num) {
            this.num = num;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public boolean isChromas() {
            return chromas;
        }

        public void setChromas(boolean chromas) {
            this.chromas = chromas;
        }
    }

    public static class Info {
        private int attack;
        private int defense;
        private int magic;
        private int difficulty;

        // Getters and Setters
        public int getAttack() {
            return attack;
        }

        public void setAttack(int attack) {
            this.attack = attack;
        }

        public int getDefense() {
            return defense;
        }

        public void setDefense(int defense) {
            this.defense = defense;
        }

        public int getMagic() {
            return magic;
        }

        public void setMagic(int magic) {
            this.magic = magic;
        }

        public int getDifficulty() {
            return difficulty;
        }

        public void setDifficulty(int difficulty) {
            this.difficulty = difficulty;
        }
    }

    public static class Stats {
        private int hp;
        private int hpperlevel;
        private int mp;
        private int mpperlevel;
        private int movespeed;
        private int armor;
        private int armorperlevel;
        private int spellblock;
        private int spellblockperlevel;
        private int attackrange;
        private double hpregen;
        private double hpregenperlevel;
        private double mpregen;
        private double mpregenperlevel;
        private double crit;
        private double critperlevel;
        private double attackdamage;
        private double attackdamageperlevel;
        private double attackspeedperlevel;
        private double attackspeed;

        // Getters and Setters
        public int getHp() {
            return hp;
        }

        public void setHp(int hp) {
            this.hp = hp;
        }

        public int getHpperlevel() {
            return hpperlevel;
        }

        public void setHpperlevel(int hpperlevel) {
            this.hpperlevel = hpperlevel;
        }

        public int getMp() {
            return mp;
        }

        public void setMp(int mp) {
            this.mp = mp;
        }

        public int getMpperlevel() {
            return mpperlevel;
        }

        public void setMpperlevel(int mpperlevel) {
            this.mpperlevel = mpperlevel;
        }

        public int getMovespeed() {
            return movespeed;
        }

        public void setMovespeed(int movespeed) {
            this.movespeed = movespeed;
        }

        public int getArmor() {
            return armor;
        }

        public void setArmor(int armor) {
            this.armor = armor;
        }

        public int getArmorperlevel() {
            return armorperlevel;
        }

        public void setArmorperlevel(int armorperlevel) {
            this.armorperlevel = armorperlevel;
        }

        public int getSpellblock() {
            return spellblock;
        }

        public void setSpellblock(int spellblock) {
            this.spellblock = spellblock;
        }

        public int getSpellblockperlevel() {
            return spellblockperlevel;
        }

        public void setSpellblockperlevel(int spellblockperlevel) {
            this.spellblockperlevel = spellblockperlevel;
        }

        public int getAttackrange() {
            return attackrange;
        }

        public void setAttackrange(int attackrange) {
            this.attackrange = attackrange;
        }

        public double getHpregen() {
            return hpregen;
        }

        public void setHpregen(double hpregen) {
            this.hpregen = hpregen;
        }
    }
    public static class Spell {
        private String id;
        private String name;
        private String description;
        private String tooltip;
        private Leveltip leveltip;
        private int maxrank;
        private List<Double> cooldown;
        private String cooldownBurn;
        private List<Integer> cost;
        private String costBurn;
        private String costType;
        private String maxammo;
        private List<Integer> range;
        private String rangeBurn;
        private Image image;
        private String resource;

        // Getters and Setters
        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getDescription() {
            return description;
        }

        public void setDescription(String description) {
            this.description = description;
        }

        public String getTooltip() {
            return tooltip;
        }

        public void setTooltip(String tooltip) {
            this.tooltip = tooltip;
        }

        public Leveltip getLeveltip() {
            return leveltip;
        }

        public void setLeveltip(Leveltip leveltip) {
            this.leveltip = leveltip;
        }

        public int getMaxrank() {
            return maxrank;
        }

        public void setMaxrank(int maxrank) {
            this.maxrank = maxrank;
        }

        public List<Double> getCooldown() {
            return cooldown;
        }

        public void setCooldown(List<Double> cooldown) {
            this.cooldown = cooldown;
        }

        public String getCooldownBurn() {
            return cooldownBurn;
        }

        public void setCooldownBurn(String cooldownBurn) {
            this.cooldownBurn = cooldownBurn;
        }

        public List<Integer> getCost() {
            return cost;
        }

        public void setCost(List<Integer> cost) {
            this.cost = cost;
        }

        public String getCostBurn() {
            return costBurn;
        }

        public void setCostBurn(String costBurn) {
            this.costBurn = costBurn;
        }

        public String getCostType() {
            return costType;
        }

        public void setCostType(String costType) {
            this.costType = costType;
        }

        public String getMaxammo() {
            return maxammo;
        }

        public void setMaxammo(String maxammo) {
            this.maxammo = maxammo;
        }

        public List<Integer> getRange() {
            return range;
        }

        public void setRange(List<Integer> range) {
            this.range = range;
        }

        public String getRangeBurn() {
            return rangeBurn;
        }

        public void setRangeBurn(String rangeBurn) {
            this.rangeBurn = rangeBurn;
        }

        public Image getImage() {
            return image;
        }

        public void setImage(Image image) {
            this.image = image;
        }

        public String getResource() {
            return resource;
        }

        public void setResource(String resource) {
            this.resource = resource;
        }

        // Leveltip class for handling the spell's leveltip
        public static class Leveltip {
            private List<String> label;
            private List<String> effect;

            // Getters and Setters
            public List<String> getLabel() {
                return label;
            }

            public void setLabel(List<String> label) {
                this.label = label;
            }

            public List<String> getEffect() {
                return effect;
            }

            public void setEffect(List<String> effect) {
                this.effect = effect;
            }
        }
    }

    // Passive class
    public static class Passive {
        private String name;
        private String description;
        private Image image;

        // Getters and Setters
        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getDescription() {
            return description;
        }

        public void setDescription(String description) {
            this.description = description;
        }

        public Image getImage() {
            return image;
        }

        public void setImage(Image image) {
            this.image = image;
        }
    }
}
