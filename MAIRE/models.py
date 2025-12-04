import sqlmodel
from typing import List, Optional


class Species(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    name: str
    genes: List["Gene"] = sqlmodel.Relationship(back_populates="species")


class Gene(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    chromosome: str
    start: int
    end: int
    strand: str
    symbol: str = sqlmodel.Field(index=True)
    ensembly_id: str
    species: Optional["Species"] = sqlmodel.Relationship(back_populates="genes")
    transcripts: List["Transcript"] = sqlmodel.Relationship(back_populates="gene")
    rnaediting: Optional[List["RNAediting"]] = sqlmodel.Relationship(
        back_populates="gene"
    )
    species_id: int | None = sqlmodel.Field(foreign_key="species.id")


class Transcript(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    transcript_id: str
    chromosome: str
    start: int
    end: int
    transcript_type: str
    gene: Optional["Gene"] = sqlmodel.Relationship(back_populates="transcripts")
    cdses: List["Cds"] = sqlmodel.Relationship(back_populates="transcript")
    utres: List["Utr"] = sqlmodel.Relationship(back_populates="transcript")
    aminochanges: Optional[List["Aminochange"]] = sqlmodel.Relationship(
        back_populates="transcript"
    )
    gene_id: int | None = sqlmodel.Field(foreign_key="gene.id")


class Cds(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    chromosome: str
    start: int
    end: int
    transcript: Optional["Transcript"] = sqlmodel.Relationship(back_populates="cdses")
    transcript_id: int | None = sqlmodel.Field(foreign_key="transcript.id")


class Utr(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    chromosome: str
    start: int
    end: int
    transcript: Optional["Transcript"] = sqlmodel.Relationship(back_populates="utres")
    transcript_id: int | None = sqlmodel.Field(foreign_key="transcript.id")


class Aminochange(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    change: str
    transcript_id: int | None = sqlmodel.Field(foreign_key="transcript.id")
    transcript: Optional["Transcript"] = sqlmodel.Relationship(
        back_populates="aminochanges"
    )
    rnaediting_id: int | None = sqlmodel.Field(foreign_key="rnaediting.id")
    rnaediting: Optional["RNAediting"] = sqlmodel.Relationship(
        back_populates="aminochanges"
    )


class RNAediting(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    chromosome: str = sqlmodel.Field(index=True)
    position: int
    ref: str
    alt: str
    location: str
    repeat_id: int | None = sqlmodel.Field(foreign_key="repeat.id")
    repeat: Optional["Repeat"] = sqlmodel.Relationship(back_populates="rnaediting")
    gene_id: int | None = sqlmodel.Field(foreign_key="gene.id")
    gene: Optional["Gene"] = sqlmodel.Relationship(back_populates="rnaediting")
    region: str
    exfun: str
    aminochanges: Optional[List["Aminochange"]] = sqlmodel.Relationship(
        back_populates="rnaediting"
    )
    samplenumbers: int
    tissuenumbers: int
    tissues: Optional[List["RNAeditingtissuelink"]] = sqlmodel.Relationship(
        back_populates="rnaediting"
    )
    editinglevel: Optional[List["EditingLevel"]] = sqlmodel.Relationship(
        back_populates="rnaediting"
    )


class Repeat(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    rnaediting: List["RNAediting"] = sqlmodel.Relationship(back_populates="repeat")
    repeatclass: str


class RNAeditingtissuelink(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    rnaediting_id: int | None = sqlmodel.Field(foreign_key="rnaediting.id")
    rnaediting: Optional["RNAediting"] = sqlmodel.Relationship(back_populates="tissues")
    tissue_id: int | None = sqlmodel.Field(foreign_key="tissue.id")
    tissue: Optional["Tissue"] = sqlmodel.Relationship(back_populates="rnaediting")


class Tissue(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    name: str
    rnaediting: List["RNAeditingtissuelink"] = sqlmodel.Relationship(
        back_populates="tissue"
    )
    editinglevel: Optional[List["EditingLevel"]] = sqlmodel.Relationship(
        back_populates="tissue"
    )
    organ_id: int | None = sqlmodel.Field(foreign_key="organ.id")
    organ: Optional["Organ"] = sqlmodel.Relationship(back_populates="tissues")


class Organ(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    name: str
    tissues: List["Tissue"] = sqlmodel.Relationship(back_populates="organ")


class EditingLevel(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(default=None, primary_key=True)
    rnaediting_id: int | None = sqlmodel.Field(foreign_key="rnaediting.id")
    tissue_id: int | None = sqlmodel.Field(foreign_key="tissue.id")
    rnaediting: Optional["RNAediting"] = sqlmodel.Relationship(
        back_populates="editinglevel"
    )
    tissue: Optional["Tissue"] = sqlmodel.Relationship(back_populates="editinglevel")
    level: float
